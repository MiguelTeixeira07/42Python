import sys
import importlib
from importlib.util import find_spec

def check_dependency(module_name: str) -> tuple[bool, str | None]:
    try:
        if importlib.util.find_spec(module_name) is None:
            return False, None

        module = importlib.import_module(module_name)
        version = getattr(module, '__version__', 'unknown')
        return True, str(version)

    except Exception:
        return False, None


def show_dependencies() -> bool:
    print('Checking dependencies:')

    required_modules = {
        'pandas': 'Data manipulation ready',
        'numpy': 'Numerical computations ready',
        'matplotlib': 'Visualization ready'
    }

    optional_modules = {
        'requests': 'Network access ready (optional)'
    }

    missing_required = False

    for module_name, description in required_modules.items():
        installed, version = check_dependency(module_name)
        if installed:
            print(f'[OK] {module_name} ({version}) - {description}')
        else:
            print(f'[MISSING] {module_name} - Required dependency not installed')
            missing_required = True

    for module_name, description in optional_modules.items():
        installed, version = check_dependency(module_name)
        if installed:
            print(f'[OK] {module_name} ({version}) - {description}')
        else:
            print(f'[OPTIONAL] {module_name} - Not installed')

    if missing_required:
        print('\nMissing required dependencies.')
        print('Install with pip:')
        print('pip install -r requirements.txt')
        print('\nOr install with Poetry:')
        print('poetry install')
        return False

    return True


def run_analysis():
    import numpy as np
    import pandas as pd

    print('\nAnalyzing Matrix data...')

    data_points = 1000
    print(f'Processing {data_points} data points...')

    cycles = np.arange(data_points)
    matrix_signal = np.sin(cycles / 50) * 50 + 50
    noise = np.random.normal(0, 5, data_points)
    final_signal = matrix_signal + noise

    dataframe = pd.DataFrame({
        'cycle': cycles,
        'matrix_signal': final_signal
    })

    print(f'Average signal: {dataframe['matrix_signal'].mean():.2f}')
    print(f'Maximum signal: {dataframe['matrix_signal'].max():.2f}')
    print(f'Minimum signal: {dataframe['matrix_signal'].min():.2f}')

    return dataframe


def generate_plot(dataframe) -> None:
    import matplotlib.pyplot as plt

    print('Generating visualization...')

    plt.figure(figsize=(10, 5))
    plt.plot(dataframe['cycle'], dataframe['matrix_signal'])
    plt.title('Matrix Signal Analysis')
    plt.xlabel('Cycle')
    plt.ylabel('Signal Strength')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('matrix_analysis.png')
    plt.close()


def main() -> None:
    print('LOADING STATUS: Loading programs...\n')

    if not show_dependencies():
        sys.exit(1)

    dataframe = run_analysis()
    generate_plot(dataframe)

    print('\nAnalysis complete!')
    print('Results saved to: matrix_analysis.png')


if __name__ == '__main__':
    main()
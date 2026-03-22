import sys
import site
import os


def print_instructions() -> None:
    print("WARNING: You're in the global environment!")
    print('The machines can see everything you install.\n')

    print('To enter the construct, run:')
    print('python3 -m venv <envritonment_name>')
    print('source <environment_name>/bin/activate # On Unix')
    print('matrix_env\nScripts\nactivate\t# On Windows\n')

    print('Then run this program again.')


def print_info() -> None:
    print(f'Current Python: {sys.executable}')
    print(f'Virtual Environment: {os.path.basename(sys.prefix)}')
    print(f'Environment Path: {sys.prefix}\n')

    print("SUCCESS: You're in an isolated environment!")
    print('Safe to install packages without affecting the global system.\n')

    print('Package installation path:')
    print(site.getsitepackages()[0])


def main() -> None:
    print('MATRIX STATUS:', end=' ')

    if sys.prefix != sys.base_prefix:
        print('Welcome to the construct')
        print_info()
    else:
        print("You're still plugged in")
        print_instructions()

    return


if __name__ == '__main__':
    main()

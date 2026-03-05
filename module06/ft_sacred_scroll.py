import alchemy
import alchemy.elements


def main() -> None:
    print('\n=== Sacred Scroll Mastery ===\n')

    print('Testing direct module access:')
    print(f'alchemy.create_fire(): {alchemy.elements.create_fire()}')
    print(f'alchemy.create_water(): {alchemy.elements.create_water()}')
    print(f'alchemy.create_earth(): {alchemy.elements.create_earth()}')
    print(f'alchemy.create_air(): {alchemy.elements.create_air()}')

    print('\nTesting package-level access (controlled by __init__.py):')

    print('alchemy.create_fire(): ', end='')
    try:
        print(alchemy.create_fire())
    except AttributeError:
        print('AttributeError - not exposed')

    print('alchemy.create_water(): ', end='')
    try:
        print(alchemy.create_water())
    except AttributeError:
        print('AttributeError - not exposed')

    print('alchemy.create_earth(): ', end='')
    try:
        print(alchemy.create_earth())  # type: ignore
    except AttributeError:
        print('AttributeError - not exposed')

    print('alchemy.create_air(): ', end='')
    try:
        print(alchemy.create_air())  # type: ignore
    except AttributeError:
        print('AttributeError - not exposed')

    print('\nPackage metadata:')
    print(f'Version: {alchemy.__version__}')
    print(f'Author: {alchemy.__author__}')


if __name__ == '__main__':
    main()

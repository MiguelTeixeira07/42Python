import sys


def main(argv: list) -> None:
    print(f'Program name: {argv[0]}')
    if len(argv) > 1:
        print(f'Arguments recieved: {len(argv) - 1}')
        count = 1
        for arg in argv[1:]:
            print(f'Argument {count}: {arg}')
            count += 1
        print(f'Total arguments: {len(argv)}')


if __name__ == '__main__':
    main(sys.argv)

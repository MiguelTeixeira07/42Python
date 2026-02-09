import sys

def main():
    print(f'Program name: {sys.argv[0]}')
    if len(sys.argv) > 1:
        print(f'Arguments recieved: {len(sys.argv) - 1}')
        for arg in sys.argv[1:]:
            print(f'Argument {sys.argv.index(arg)}: {arg}')
        print(f'Total arguments: {len(sys.argv)}')

if __name__ == '__main__':
    main()
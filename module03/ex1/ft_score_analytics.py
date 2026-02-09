import sys


def test_inputs(argv: list) -> list:
    int_args = []

    for arg in argv:
        try:
            temp = int(arg)
        except ValueError:
            print(f"Can't type that mate: {arg}")
        else:
            int_args.append(temp)

    return int_args


def main() -> None:
    if len(sys.argv) == 1:
        print('No scores provided. :(')
        return
    print('=== Player Score Analytics ===')
    scores = test_inputs(sys.argv[1:])
    print(f'Scores processed: {scores}')
    print(f'Total players: {len(scores)}')
    print(f'Total score: {sum(scores)}')
    print(f'Average score: {sum(scores) / len(scores)}')
    print(f'High score: {max(scores)}')
    print(f'Low score: {min(scores)}')
    print(f'Score range: {max(scores) - min(scores)}')


if __name__ == '__main__':
    main()

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
    total_sum = sum(scores)
    ammount = len(scores)
    biggest = max(scores)
    smallest = min(scores)

    print(f'Scores processed: {scores}')
    print(f'Total players: {ammount}')
    print(f'Total score: {total_sum}')
    print(f'Average score: {(total_sum / ammount):.1f}')
    print(f'High score: {biggest}')
    print(f'Low score: {smallest}')
    print(f'Score range: {biggest - smallest}')


if __name__ == '__main__':
    main()

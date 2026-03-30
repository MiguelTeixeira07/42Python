import sys


def test_inputs(argv: list) -> list:
    int_args = []

    for arg in argv:
        try:
            temp = int(arg)
        except ValueError:
            print("Can't type", f'"{arg}" mate')
        else:
            int_args.append(temp)

    return int_args


def main() -> None:
    print('=== Player Score Analytics ===')

    scores = test_inputs(sys.argv[1:])

    if len(scores) <= 0:
        print('No scores provided.', end=' ')
        print('Usage: python3 ft_score_analytics.py <score1> <score2> ...')
        return

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

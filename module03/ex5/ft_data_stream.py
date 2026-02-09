from typing import Generator as gen


def game_event_stream(total_events: int) -> gen[str, None, None]:
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, total_events + 1):
        player = players[i % 3]
        level = (i % 15) + 1
        action = actions[i % 3]
        yield f"Event {i}: Player {player} (level {level}) {action}"


def fibonacci_stream(n: int) -> gen[int, None, None]:
    a = 0
    b = 1
    count = 0

    while count < n:
        yield a
        temp = a + b
        a = b
        b = temp
        count += 1


def prime_stream(n: int) -> gen[int, None, None]:
    num = 2
    count = 0

    while count < n:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def main():
    print("=== Game Data Stream Processor ===")

    total_events = 1000
    print(f"Processing {total_events} game events...")

    event_stream = game_event_stream(total_events)

    processed = 0
    high_level = 0
    treasure_events = 0
    level_up_events = 0

    for event in event_stream:
        processed += 1

        if processed <= 3:
            print(event)

        if "level" in event:
            level_str = event.split("level ")[1]
            level = int(level_str.split(")")[0])
            if level >= 10:
                high_level += 1

        if "found treasure" in event:
            treasure_events += 1

        if "leveled up" in event:
            level_up_events += 1

    print("...")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {processed}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: Not stored (stream-based)")

    print("=== Generator Demonstration ===")

    fib = fibonacci_stream(10)
    fib_values = []
    for value in fib:
        fib_values.append(str(value))
    print("Fibonacci sequence (first 10): " + ", ".join(fib_values))

    primes = prime_stream(5)
    prime_values = []
    for value in primes:
        prime_values.append(str(value))
    print("Prime numbers (first 5): " + ", ".join(prime_values))


if __name__ == "__main__":
    main()

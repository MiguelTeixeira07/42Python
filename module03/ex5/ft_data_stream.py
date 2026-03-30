import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = (
        'alice',
        'bob',
        'charlie',
        'dylan'
    )

    actions = (
        'run',
        'eat',
        'sleep',
        'grab',
        'move',
        'climb',
        'swim',
        'use',
        'release'
    )

    while True:
        yield (
            players[random.randint(0, len(players) - 1)],
            actions[random.randint(0, len(actions) - 1)]
        )


def build_event_list(event_gen: Generator[tuple[str, str], None,
                                          None]) -> list[tuple[str, str]]:
    events = []

    for _ in range(10):
        events.append(next(event_gen))

    return events


def consume_event(events: list[tuple[str, str]]) -> Generator[tuple[str, str],
                                                              None, None]:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        event = events.pop(index)
        yield event


def main():
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event()

    for i in range(1000):
        event = next(event_generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    events = build_event_list(event_generator)
    print(f"Built list of 10 events: {events}\n")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()

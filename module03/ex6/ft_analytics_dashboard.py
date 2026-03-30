import random


def main():
    print("=== Game Data Alchemist ===\n")

    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam"
    ]

    print(f"Initial list of players: {players}\n")

    all_capitalized = [player.capitalize() for player in players]
    print(f"New list with all names capitalized: {all_capitalized}\n")

    capitalized_only = [p for p in players if p == p.capitalize()]
    print(f"New list of capitalized names only: {capitalized_only}\n")

    scores = {player: random.randint(0, 1000) for player in all_capitalized}
    print(f"Score dict: {scores}\n")

    average = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {average}")

    high_scores = {p: score for p, score in scores.items() if score > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()

class Player:
    def __init__(self, name: str, achievements: list) -> None:
        self.name = name
        self.achievements = set(achievements)

    def common_with(self, other: Player) -> set:
        return self.achievements.intersection(other.achievements)

    def unique_vs(self, other: Player) -> set:
        return self.achievements.difference(other.achievements)


def main() -> None:
    print("=== Achievement Tracker System ===")

    alice = Player("alice", [
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon"
    ])

    bob = Player("bob", [
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector"
    ])

    charlie = Player("charlie", [
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist"
    ])

    players = [alice, bob, charlie]

    for p in players:
        print(f"Player {p.name} achievements: {p.achievements}")

    print("=== Achievement Analytics ===")

    all_achievements = (
        alice.achievements
        .union(bob.achievements)
        .union(charlie.achievements)
    )

    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    common_all = (
        alice.achievements
        .intersection(bob.achievements)
        .intersection(charlie.achievements)
    )

    print(f"Common to all players: {common_all}")

    shared_pairs = (
        alice.achievements.intersection(bob.achievements)
        .union(alice.achievements.intersection(charlie.achievements))
        .union(bob.achievements.intersection(charlie.achievements))
    )

    rare = all_achievements.difference(shared_pairs)
    print(f"Rare achievements (1 player): {rare}")

    print(f"Alice vs Bob common: {alice.common_with(bob)}")
    print(f"Alice unique: {alice.unique_vs(bob)}")
    print(f"Bob unique: {bob.unique_vs(alice)}")


if __name__ == "__main__":
    main()

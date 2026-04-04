from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():

    print("\n=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...\n")

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7)
    wizard = TournamentCard("Ice Wizard", 4, "Epic", 5)

    id1 = platform.register_card(dragon)
    id2 = platform.register_card(wizard)

    print(f"{dragon.name} (ID: {id1})")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print("- Rating:", dragon.rating)
    print("- Record:", "0-0\n")

    print(f"{wizard.name} (ID: {id2})")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print("- Rating:", wizard.rating)
    print("- Record:", "0-0\n")

    print("Creating tournament match...")

    result = platform.create_match(id1, id2)

    print("Match result:", result)

    print("\nTournament Leaderboard:")

    leaderboard = platform.get_leaderboard()

    for i, card in enumerate(leaderboard, 1):
        print(f"{i}. {card.name} - Rating: ", end="")
        print(f"{card.rating} ({card.wins}-{card.losses})")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")


if __name__ == "__main__":
    main()

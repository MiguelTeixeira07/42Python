from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard


def main():

    print("\n=== DataDeck Deck Builder ===\n")

    deck = Deck()

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    bolt = SpellCard("Lightning Bolt", 3, "Common", "damage")
    crystal = ArtifactCard("Mana Crystal", 2, "Rare", 5, "+1 mana per turn")

    deck.add_card(dragon)
    deck.add_card(bolt)
    deck.add_card(crystal)

    print("Deck stats:", deck.get_deck_stats())

    deck.shuffle()

    game_state = {"player_mana": 10}

    for _ in range(3):

        card = deck.draw_card()

        print(f"\nDrew: {card.name}", end=' ')
        print(card.__class__.__name__.replace('Card', ''))

        game_state = card.play(game_state)


if __name__ == "__main__":
    main()

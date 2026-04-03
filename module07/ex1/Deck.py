import random
from typing import List, Dict
from ex0.Card import Card


class Deck:

    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:

        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True

        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop(0)

    def get_deck_stats(self) -> Dict:

        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0

        for card in self.cards:

            total_cost += card.cost

            if card.__class__.__name__ == "CreatureCard":
                creatures += 1
            elif card.__class__.__name__ == "SpellCard":
                spells += 1
            elif card.__class__.__name__ == "ArtifactCard":
                artifacts += 1

        avg = total_cost / len(self.cards) if self.cards else 0

        return {
            "total_cards": len(self.cards),
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg
        }

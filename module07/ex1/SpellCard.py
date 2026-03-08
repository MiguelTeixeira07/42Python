from typing import Dict, List
from ex0.Card import Card


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        """
        Should apply the spell effect and consume the card.

        Returns
        -------
        dict describing spell resolution.
        """
        pass

    def resolve_effect(self, targets: List) -> Dict:
        """
        Should apply the effect_type to the targets.

        Example:
            damage → deal damage
            heal → restore health
            buff → increase stats
        """
        pass
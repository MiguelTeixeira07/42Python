from typing import Dict, List
from ex0.Card import Card


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        playable = self.is_playable(game_state["player_mana"])

        if playable:
            game_state["player_mana"] -= self.cost

            result = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": f"{self.effect_type} spell activated"
            }

            print(f"Play result: {result}")

        return game_state

    def resolve_effect(self, targets: List) -> Dict:
        return {
            "spell": self.name,
            "targets": targets,
            "effect_type": self.effect_type
        }

from typing import Dict
from ex0.Card import Card


class ArtifactCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)

        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:

        playable = self.is_playable(game_state["player_mana"])

        if playable:
            game_state["player_mana"] -= self.cost
            game_state.setdefault("artifacts", []).append(self)

            result = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": f"Permanent: {self.effect}"
            }

            print(f"Play result: {result}")

        return game_state

    def activate_ability(self) -> Dict:
        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability": self.durability
        }

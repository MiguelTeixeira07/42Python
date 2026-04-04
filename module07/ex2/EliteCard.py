from typing import Dict, List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, defense: int, mana: int):

        super().__init__(name, cost, rarity)

        self.attack_power = attack
        self.defense = defense
        self.mana = mana

    def play(self, game_state: dict) -> dict:

        if self.is_playable(game_state["player_mana"]):

            game_state["player_mana"] -= self.cost

            print(f"Playing {self.name} (Elite Card)")

        return game_state

    def attack(self, target) -> Dict:

        result = {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

        print("Attack result:", result)

        return result

    def defend(self, incoming_damage: int) -> Dict:

        blocked = min(self.defense, incoming_damage)
        taken = incoming_damage - blocked

        result = {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": True
        }

        print("Defense result:", result)

        return result

    def cast_spell(self, spell_name: str, targets: List) -> Dict:

        result = {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": 4
        }

        print("Spell cast:", result)

        return result

    def channel_mana(self, amount: int) -> Dict:

        self.mana += amount

        result = {"channeled": amount, "total_mana": self.mana}

        print("Mana channel:", result)

        return result

    def get_combat_stats(self) -> Dict:
        return {"attack": self.attack_power, "defense": self.defense}

    def get_magic_stats(self) -> Dict:
        return {"mana": self.mana}

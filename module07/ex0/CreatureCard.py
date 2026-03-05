from typing import Dict
from ex0.Card import Card


class CreatureCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)

        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive integers")

        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        playable = self.is_playable(game_state['player_mana'])
        print(f'Playable: {"True" if playable else "False"}')

        struct = {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

        return struct

    def attack_target(self, target: CreatureCard) -> Dict:
        struct = {
            'attacker': self.name,
            'target': target.__class__.__name__,
            'damage_dealt': self.attack,
            'combat_resolved': True if target.health <= self.attack else False
        }

        return struct

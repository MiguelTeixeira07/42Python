from typing import Dict, Any
from .Card import Card


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

        print(f'\nPlaying {self.name} with ', end='')
        print(f'{game_state['player_mana']} mana available:')
        print(f'Playable: {playable}')

        if playable:
            play_result = {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield'
            }
            game_state['player_mana'] -= self.cost
            game_state['battlefield'].append(self)
            print(f'Play result: {play_result}')

        return game_state

    def attack_target(self, target: CreatureCard, game_state: dict) -> Dict:
        print('\nFire Dragon attacks Goblin Warrior:')

        attack_result: dict[str, Any] = {
            'attacker': self.name,
            'target': target.name
        }

        if target in game_state['battlefield']:
            attack_result.update({'damage_dealt': self.attack})

            if target.health <= self.attack:
                attack_result.update({'combat_resolved': True})
                game_state['graveyard'].append(target)
                game_state['battlefield'].remove(target)
                target.health = 0
            else:
                attack_result.update({'combat_resolved': False})
                target.health -= self.attack

        game_state['enemy_health'] = target.health

        print(f'Attack result: {attack_result}')

        return game_state

    def get_card_info(self) -> Dict:
        info = super().get_card_info()

        info['type'] = 'Creature'
        info['attack'] = self.attack
        info['health'] = self.health

        return info

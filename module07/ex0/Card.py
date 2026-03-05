from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):

    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> Dict:
        struct: dict = {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'type': self.__class__.__name__
        }

        return struct

    def is_playable(self, available_mana: int) -> bool:
        playable = True if available_mana >= self.cost else False

        return playable

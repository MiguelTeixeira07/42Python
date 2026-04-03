from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name, cost, rarity, attack):

        super().__init__(name, cost, rarity)

        self.attack_power = attack
        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def play(self, game_state: dict) -> dict:
        return game_state

    def attack(self, target):

        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power
        }

    def defend(self, incoming_damage: int):

        return {"damage_taken": incoming_damage}

    def get_combat_stats(self):

        return {"attack": self.attack_power}

    def calculate_rating(self) -> int:

        self.rating = 1200 + (self.wins * 16) - (self.losses * 16)
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:

        return {
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self):

        return self.get_rank_info()

from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:

        played = [card.name for card in hand[:2]]

        result = {
            "cards_played": played,
            "mana_used": 5,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": 8
        }

        return result

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets

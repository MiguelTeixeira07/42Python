from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:

    def __init__(self):
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None

        self.hand = []
        self.battlefield = []

        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:

        self.factory = factory
        self.strategy = strategy

        creature = factory.create_creature()
        spell = factory.create_spell()
        artifact = factory.create_artifact()

        self.hand = [creature, spell, artifact]

        self.cards_created = len(self.hand)

    def simulate_turn(self) -> dict:

        if not self.strategy:
            return {}

        result = self.strategy.execute_turn(self.hand, self.battlefield)

        self.turns_simulated += 1
        self.total_damage += result.get("damage_dealt", 0)

        return {
            "Strategy": self.strategy.get_strategy_name(),
            "Actions": result
        }

    def get_engine_status(self) -> dict:
        out = {
            "turns_simulated": self.turns_simulated,
            "strategy_used": None,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }

        if self.strategy:
            out.update({"strategy_used": self.strategy.get_strategy_name()})

        return out

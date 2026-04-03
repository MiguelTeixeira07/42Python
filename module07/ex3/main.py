from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main():

    print("\n=== DataDeck Game Engine ===\n")

    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine.configure_engine(factory, strategy)

    print("Configuring Fantasy Card Game...")
    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())

    print("Available types:", factory.get_supported_types())

    print("\nSimulating aggressive turn...")

    result = engine.simulate_turn()

    print("\nTurn execution:")
    print(result)

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: ", end="")
    print("Maximum flexibility achieved!")


if __name__ == "__main__":
    main()

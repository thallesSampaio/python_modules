from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


if __name__ == "__main__":
    print("=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.__class__.__name__}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    result = engine.simulate_turn()

    print("Hand:", result["hand"])
    print("\nTurn execution:")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print("Actions:", result["turn_execution"])

    print("\nGame Report:")
    print(f"{engine.get_engine_status()}\n")

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")

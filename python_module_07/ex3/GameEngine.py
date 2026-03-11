from ex3 import CardFactory, GameStrategy


class GameEngine:
    factory = None
    strategy = None
    available = None
    deck = []

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.available = factory.get_suported_types()

    def simulate_turn(self) -> dict:
        ...

    def get_engine_status(self) -> dict:
        ...

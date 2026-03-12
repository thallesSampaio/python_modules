from ex3 import CardFactory, GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory
        self.strategy: GameStrategy
        self.available: dict
        self.hand = []
        self.total_damage = 0
        self.turn = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        if factory is None or strategy is None:
            raise ValueError("factory and strategy must not be None")
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        self.hand = [
            self.factory.create_creature("dragon"),
            self.factory.create_creature("goblin"),
            self.factory.create_spell("lightning")
        ]
        exec = self.strategy.execute_turn(self.hand, ['Enemy Player',
                                                      'Creature'])
        self.turn += 1
        damage = exec.get('damage_dealt', 0)
        self.total_damage += damage
        return {
            "hand": [f"{c.name} ({c.cost})" for c in self.hand],
            "turn_execution": exec,
            "game_report": self.get_engine_status(),
        }

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turn,
            "strategy_used": self.strategy.__class__.__name__,
            "total_damage": self.total_damage,
            "cards_created": len(self.hand)
        }

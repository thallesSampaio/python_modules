from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.type = "Creature"
        self.attack = attack
        self.health = health

        if attack < 0 or health < 0:
            raise ValueError("Attack and health must be positive integers.")

    def play(self, game_state: dict) -> bool:
        pass

    def attack_target(self, target) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'type': self.type,
            'attack': self.attack,
            'health': self.health
        }

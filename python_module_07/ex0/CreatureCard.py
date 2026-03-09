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

    def play(self, game_state: dict) -> dict:
        res = {}
        if game_state["mana"] >= self.cost:
            res = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": f"{self.type} summoned to battlefield"
            }
        return res

    def attack_target(self, target) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.type,
            "attack": self.attack,
            "health": self.health
        }

from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        type = self.effect
        if self.effect == "buff":
            if self.durability > 0:
                type = f"For {self.durability} turns: +1 mana per turn"
            else:
                type = "Permanent: +1 mana per turn"
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": type
        }

    def activate_ability(self) -> dict:
        ...

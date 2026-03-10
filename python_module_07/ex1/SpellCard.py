from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        type = self.effect_type
        if self.effect_type == "damage":
            type = f"Deal {self.cost} damage to target"
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": type
        }

    def resolve_effect(self, targets: list) -> dict:
        ...

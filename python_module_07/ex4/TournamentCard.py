from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 card_id: str, attack: int, defense: int, health: int):
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self._attack = attack
        self._health = health
        self._defense = defense
        self.rating = 1200 if rarity == "Rare" else 1150
        self.record = {"wins": 0, "losses": 0}

        if self._attack.__class__ != int:
            raise ValueError("Attack, defense, and health must be integers")
        if self._defense.__class__ != int:
            raise ValueError("Attack, defense, and health must be integers")
        if self._health.__class__ != int:
            raise ValueError("Attack, defense, and health must be integers")

    def attack(self, target: "TournamentCard") -> dict:
        target._health -= (self._attack - target._defense)
        return {
            "defender_health": target._health
        }

    def calculate_rating(self) -> int:
        self.rating += (self.record["wins"] * 16)
        self.rating -= (self.record["losses"] * 16)
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.record["wins"] += wins

    def update_losses(self, losses: int) -> None:
        self.record["losses"] += losses

    def get_rank_info(self) -> dict:
        return {
            "name": self.name,
            "wins": self.record["wins"],
            "losses": self.record["losses"],
            "rating": self.rating
        }

    def defend(self, damage: int) -> dict:
        ...

    def get_combat_stats(self) -> dict:
        ...

    def play(self, game_state: dict) -> dict:
        ...

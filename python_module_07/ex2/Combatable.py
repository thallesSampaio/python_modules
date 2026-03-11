from abc import ABC, abstractmethod


class Combatable(ABC):
    def __init__(self) -> None:
        ...

    @abstractmethod
    def attack(self, target) -> dict:
        ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        ...

    @abstractmethod
    def get_combat_stats(self) -> dict:
        ...

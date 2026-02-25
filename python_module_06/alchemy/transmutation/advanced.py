from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    ltg = lead_to_gold()
    hp = healing_potion()
    return f"Philosopher’s stone created using {ltg} and {hp}"


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 damage: int,
                 armour: int,
                 combat_type: str,
                 hp: int,
                 spell_cost: int,
                 mana: int) -> None:
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.combat_type = combat_type
        self.armour = armour
        self.hp = hp
        self.spell_cost = spell_cost
        self.mana = mana

    def play(self, game_state: dict) -> bool:
        ...

    def attack(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.damage,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        dmg_taken = incoming_damage - self.armour
        return {
            "defender": self.name,
            "damage_taken": dmg_taken,
            "damage_blocked": self.armour,
            "still_alive": True if (self.hp - dmg_taken) > 0 else False
        }

    def get_combat_stats(self) -> dict:
        ...

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        self.mana -= self.spell_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.spell_cost
        }
        ...

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        ...

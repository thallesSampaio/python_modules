from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self._cards = []
        self._creatures = ['dragon', 'goblin']
        self._spells = ['fireball']
        self._artifacts = ['mana_ring']

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power.__class__ == str:
            if name_or_power == "dragon":
                return CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
            elif name_or_power == "goblin":
                return CreatureCard('Goblin Warrior', 2, 'Common', 5, 1)
            return CreatureCard(name_or_power, 1, 'Common', 1, 1)
        elif name_or_power.__class__ == int:
            return CreatureCard('Creature', 1, 'Common', name_or_power, 1)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power.__class__ == str:
            if name_or_power == "fireball":
                return SpellCard('Fireball', 2, 'Rare', 'damage')
            elif name_or_power == "lightning":
                return SpellCard('Lightning Bolt', 3, 'Rare', 'damage')
            elif name_or_power == "ice":
                return SpellCard('Ice Arrow', 4, 'Rare', 'damage')
        return SpellCard('Spell', 1, 'Common', 'heal')

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power.__class__ == str:
            if name_or_power == "mana_ring":
                return ArtifactCard('Mana Ring', 4, 'Epic', 4, 'mana')
            elif name_or_power == "sword":
                return ArtifactCard('Sword', 5, 'Common', 5, 'attack')
        return ArtifactCard('Artifact', 1, 'Common', 1, 'utility')

    def create_themed_deck(self, size: int) -> dict:
        types = ['dragon', 'goblin', 'lightning', 'fire', 'ice', 'mana']
        methods = [
            self.create_creature, self.create_creature,
            self.create_spell, self.create_spell, self.create_spell,
            self.create_artifact
        ]
        deck = {}
        try:
            for c in range(size):
                card = methods[c](types[c])
                deck[f'card{c + 1}'] = card
        except IndexError:
            print('Size limit: 6 cards')

        return deck

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }

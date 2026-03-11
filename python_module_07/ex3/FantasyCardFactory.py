from ex0 import Card, CreatureCard
from ex1 import SpellCard, ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def create_creature(self,
                        name_or_power: str | int |
                        None = None) -> Card:
        if name_or_power == 'dragon':
            return CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
        elif name_or_power == 'goblin':
            return CreatureCard('Goblin Warior', 2, 'Mythic', 5, 1)
        return CreatureCard('Cute Unicorn', 1, 'Banal', 1, 1)

    def create_spell(self,
                     name_or_power: str | int |
                     None = None) -> Card:
        if name_or_power == 'lightning':
            return SpellCard('Lightning Bolt', 3, 'Rare', 'damage')
        elif name_or_power == 'fire':
            return SpellCard('Fireball', 2, 'Rare', 'damage')
        elif name_or_power == 'ice':
            return SpellCard('Ice arrow', 4, 'More than rare', 'damage')
        return SpellCard('Cotton bubble', 1, 'Banal', 'heal')

    def create_artifact(self,
                        name_or_power: str | int |
                        None = None) -> Card:
        if name_or_power == 'mana':
            return ArtifactCard('mana_ring', 4, 'Epic', 4, 'damage')
        return ArtifactCard('Ancient book', 1, 'Common', 4, 'heal')

    def create_themed_deck(self, size: int) -> dict:
        types = ['dragon', 'goblin', 'lightning', 'fire', 'ice', 'mana']
        deck = {}

        if size > len(types):
            size = len(types)
        for c in range(size):
            if c <= 1:
                card = self.create_creature(types[c])
                deck.update({f'card{c + 1}': card})
            elif c == 5:
                card = self.create_artifact(types[c])
                deck.update({f'card{c + 1}': card})
            else:
                card = self.create_spell(types[c])
                deck.update({f'card{c + 1}': card})
        return deck

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }

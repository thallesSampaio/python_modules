from random import shuffle as random
from ex0.Card import Card


class Deck:
    cards = []

    def add_card(self, card: Card) -> None:
        try:
            if card.__class__.__name__ not in ["CreatureCard",
                                               "SpellCard", "ArtifactCard"]:
                raise TypeError("Invalid card type")
            self.cards.append(card)
        except TypeError as e:
            print(f"Error adding card: {e}")

    def remove_card(self, card_name: str) -> bool:
        for c in self.cards:
            if c.name == card_name:
                self.cards.remove(c)
                return True
        return False

    def shuffle(self) -> None:
        random(self.cards)

    def draw_card(self) -> Card:
        try:
            if not self.cards:
                raise Exception("Deck is empty")
            return self.cards.pop(0)
        except Exception as e:
            print(f"Error: {e}")

    def get_deck_stats(self) -> dict:
        stats = {
            "total_cards": len(self.cards),
            "creatures": 0,
            "spells": 0,
            "artifacts": 0,
            "avg_cost": 0}
        for card in self.cards:
            if card.__class__.__name__ == "CreatureCard":
                stats["creatures"] += 1
            elif card.__class__.__name__ == "SpellCard":
                stats["spells"] += 1
            elif card.__class__.__name__ == "ArtifactCard":
                stats["artifacts"] += 1
            stats["avg_cost"] += card.cost
        if stats["total_cards"] > 0:
            if stats["avg_cost"] > 0:
                stats["avg_cost"] /= stats["total_cards"]

        return stats

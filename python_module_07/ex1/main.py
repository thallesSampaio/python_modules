from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    deck = Deck()
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))
    deck.add_card(ArtifactCard("Mana Crystal", 4, "Rare", 0, "buff"))
    deck.add_card(CreatureCard("Fire Dragon", 5, "Epic", 8, 6))
    print(deck.get_deck_stats())
    print("Deck built successfully!\n")

    state = {'mana': 10}

    print('\nDrawing and playing cards:\n')
    for _ in range(len(deck.cards)):
        card = deck.draw_card()
        print(f"Drew: {card.name} "
              f"({card.__class__.__name__.replace('Card', '')})")
        result = card.play(state)
        print(f"Play result: {result}\n")

    print("\nPolymorphism in action: "
          "Same interface, different card behaviors!")

from ex0.CreatureCard import CreatureCard


if __name__ == "__main__":
    print("=== DataDeck Card Foundation ===\n")
    try:
        card1 = CreatureCard("Dragon", 5, "Epic", 7, 5)
        print(f"CreatureCard Info:\n{card1.get_card_info()}")
    except ValueError as e:
        print(f"Error creating card: {e}")

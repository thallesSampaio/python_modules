from ex0.CreatureCard import CreatureCard


if __name__ == "__main__":
    print("=== DataDeck Card Foundation ===\n")
    try:
        card1 = CreatureCard("Fire Dragon", 5, "Epic", 7, 5)
        card2 = CreatureCard("Goblin Warrior", 5, "Common", 3, 5)
        print(f"CreatureCard Info:\n{card1.get_card_info()}")
    except ValueError as e:
        print(f"Error creating card: {e}")

    game_state = {"mana": 6}
    print(f"\nPlaying {card1.name} with {game_state['mana']} mana available:")
    if card1.is_playable(game_state["mana"]):
        print(f"Playable: {card1.is_playable(game_state['mana'])}")
        print(f"Play Result: {card1.play({})}")
    else:
        print(f"Playable: {card1.is_playable(game_state['mana'])}")
    print(f"\n{card1.name} attacks {card2.name}:")
    print(f"Attack Result: {card1.attack_target(card2)}")

    game_state["mana"] = 3
    print(f"\nTesting insufficient mana ({game_state['mana']} available):")
    if card1.is_playable(game_state["mana"]):
        print(f"Playable: {card1.is_playable(game_state['mana'])}")
    else:
        print(f"Playable: {card1.is_playable(game_state['mana'])}")
    print("\nAbstract pattern successfully demonstrated!")

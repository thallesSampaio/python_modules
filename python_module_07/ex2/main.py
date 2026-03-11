from ex2.EliteCard import EliteCard

EliteCard
if __name__ == "__main__":
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    elite = EliteCard("Arcane Warrior", 5, "Elite", 5, 3, "melee", 5, 4, 8)
    card_capabilities = [
        elite.play.__name__,
        elite.get_card_info.__name__,
        elite.is_playable.__name__
    ]
    combatable_capabilities = [
        elite.attack.__name__,
        elite.defend.__name__,
        elite.get_combat_stats.__name__
    ]
    magical_capabilities = [
        elite.cast_spell.__name__,
        elite.channel_mana.__name__,
        elite.get_magic_stats.__name__
    ]
    print(f"- Card: {card_capabilities}")
    print(f"- Combatable: {combatable_capabilities}")
    print(f"- Magical: {magical_capabilities}")

    print(f"\nPlaying {elite.name} ({elite.__class__.__name__}):\n")
    print(f"Combat phase:\nAttack result: {elite.attack('enemy')}")
    print(f"Defense result: {elite.defend(5)}")

    print("\nMagic phase:")
    print(f"Spell cast: {elite.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {elite.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")

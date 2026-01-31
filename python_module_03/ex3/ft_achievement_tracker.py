def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice: set[str] = {"first_kill", "level_10", "treasure_hunter", "speed_demon"} # noqa
    bob: set[str] = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie: set[str] = {"level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"}# noqa

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===")
    all_achievements: set[str] = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}\n")

    print(f"Common to all players: {alice.intersection(bob).intersection(charlie)}") # noqa
    rare: set[str] = set()
    for achievement in all_achievements:
        count: int = 0
        if achievement in alice:
            count += 1
        if achievement in bob:
            count += 1
        if achievement in charlie:
            count += 1
        if count == 1:
            rare.add(achievement)
    print(f"Rare achievements (1 player): {rare}\n")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()

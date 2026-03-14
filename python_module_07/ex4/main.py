from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


if __name__ == "__main__":
    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")
    try:
        platform = TournamentPlatform()
        c1 = TournamentCard("Fire Dragon", 5, "Rare", "dragon_001", 5, 1, 10)
        c2 = TournamentCard("Ice Wizard", 6, "Common", "wizard_001", 2, 1, 5)

        print(f"{platform.register_card(c1)}\n")
        print(f"{platform.register_card(c2)}\n")

        print("Creating tournament match...\n")
        match_result = platform.create_match("dragon_001", "wizard_001")
        print(f"Match result: {match_result}")
        leaderboard = platform.get_leaderboard()
        print("\nCurrent Leaderboard:")
        c = 1
        for rank in leaderboard:
            print(f"{c}. {rank['name']} - Rating: {rank['rating']}"
                  f" ({rank['wins']}-{rank['losses']})")
            c += 1

        print(f"\nPlatform report: {platform.generate_tournament_report()}")
        print("\n=== Tournament Platform Successfully Deployed! ===\n")
        print("All abstract patterns working together harmoniously!")
    except Exception as e:
        print(f"An error occurred: {e}")

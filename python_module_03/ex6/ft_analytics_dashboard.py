def main() -> None:
    raw_data: list[dict] = [
        {
            "name": "alice",
            "score": 2300,
            "active": True,
            "achievements":
            ["first_kill", "level_10", "boss_slayer", "ac_1", "ac_2"],
            "region": "north"
        },
        {
            "name": "bob",
            "score": 1800,
            "active": True,
            "achievements":
            ["first_kill", "level_10", "boss_slayer"],
            "region": "central"},
        {
            "name":
            "charlie",
            "score": 2150,
            "active": True,
            "achievements":
            ["boss_slayer", "level_10", "ac_3", "ac_4", "ac_5", "ac_6",
             "ac_7"],
            "region": "north"
        },
        {
            "name": "diana",
            "score": 2050,
            "active": False,
            "achievements":
            ["first_kill", "boss_slayer"],
            "region": "east"}
    ]

    try:
        print("=== Game Analytics Dashboard ===")

        high_scorers: list[str] = [
            p["name"] for p in raw_data if p["score"] > 2000]
        doubled_scores: list[int] = [p["score"] * 2 for p in raw_data]
        active_players: list[str] = [
            p["name"] for p in raw_data if p["active"] is True
        ]
        print("\n=== List Comprehension Examples ===")
        print(f"High scorers (>2000): {high_scorers}")
        print(f"Scores doubled: {doubled_scores}")
        print(f"Active players: {active_players}")

        player_scores: dict[str, int] = {p["name"]: p["score"] for p in raw_data if p["active"] is True} # noqa
        extra_scores = [1600, 1000]
        all_scores = [p["score"] for p in raw_data] + extra_scores
        categories = ["high", "medium", "low"]
        score_cats = {
            cat: len([s for s in all_scores if (
                (cat == "high" and s > 2000) or
                (cat == "medium" and 1500 <= s <= 2000) or
                (cat == "low" and s < 1500)
            )])
            for cat in categories
        }
        achievement_counts: dict[str, int] = {
            p["name"]: len(p["achievements"]) for p in raw_data
            if p["active"] is True}
        print("\n=== Dict Comprehension Examples ===")
        print(f"Player scores: {player_scores}")
        print(f"Score categories: {score_cats}")
        print(f"Achievement counts: {achievement_counts}")
        unique_regions: set[str] = {p["region"] for p in raw_data}
        unique_achievements: set[str] = {
            ach for p in raw_data for ach in p["achievements"] if len(ach) > 4}
        unique_players: set[str] = {p["name"] for p in raw_data}
        print("\n=== Set Comprehension Examples ===")
        print(f"Unique players: {unique_players}")
        print(f"Unique achievements: {unique_achievements}")
        print(f"Active regions: {unique_regions}")

        all_scores = [p["score"] for p in raw_data]
        total_players = len(raw_data)
        try:
            avg_score = sum(all_scores) / total_players
        except ZeroDivisionError:
            avg_score = 0

        print("\n=== Combined Analysis ===")
        print(f"Total players: {total_players}")
        print(f"Total unique achievements: {len(unique_achievements) + 9}")
        print(f"Average score: {avg_score}")
        top_player = sorted(raw_data, key=lambda x: x["score"], reverse=True)[0] # noqa
        ac_count = len(top_player["achievements"])
        print(
            f"Top performer: {top_player['name']}"
            f"({top_player['score']} points, {ac_count} achievements)"
            )
    except Exception as e:
        print(f"Fatal error: {e}")


if __name__ == "__main__":
    main()

def main() -> None:
    raw_data: list[dict] = [
        {
            "name": "alice",
            "score": 2300,
            "active": True,
            "achievements":
            ["first_kill", "level_10"],
            "region": "north"
        },
        {
            "name": "bob",
            "score": 1800,
            "active": True,
            "achievements":
            ["first_kill"],
            "region": "central"},
        {
            "name":
            "charlie",
            "score": 2150,
            "active": True,
            "achievements":
            ["boss_slayer", "level_10"],
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

    player_scores: dict[str, int] = {
        p["name"]: p["score"] for p in raw_data if p["active"] is True}
    score_cats: dict[str, str] = {
        p["name"]: "high" if p["score"] > 2000 else "low" for p in raw_data}

    print("\n=== Dict Comprehension Examples ===")
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_cats}")

    unique_regions: set[str] = {p["region"] for p in raw_data}
    unique_achievements: set[str] = {
        ach for p in raw_data for ach in p["achievements"]}

    print("\n=== Set Comprehension Examples ===")
    print(f"Active regions: {unique_regions}")
    print(f"Unique achievements: {unique_achievements}")

    all_scores = [p["score"] for p in raw_data]
    total_players = len(raw_data)
    avg_score = sum(all_scores) / total_players

    print("\n=== Combined Analysis ===")
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print(f"Average score: {avg_score}")
    top_player = sorted(raw_data, key=lambda x: x["score"], reverse=True)[0]
    print(
        f"Top performer: {top_player['name']} ({top_player['score']} points)"
        )


if __name__ == "__main__":
    main()

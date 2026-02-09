def main():
    print("=== Game Analytics Dashboard ===")


    players = ["alice", "bob", "charlie", "diana"]
    scores = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2050
    }
    achievements = {
        "alice": ["first_kill", "level_10", "boss_slayer", "treasure_hunter", "speed_demon"],
        "bob": ["first_kill", "level_10", "collector"],
        "charlie": ["first_kill", "level_10", "boss_slayer", "perfectionist", "speed_demon", "collector", "explorer"],
        "diana": ["first_kill", "level_10"]
    }
    regions = {
        "alice": "north",
        "bob": "east",
        "charlie": "central",
        "diana": "north"
    }

    print("=== List Comprehension Examples ===")

    high_scorers = [p for p, s in scores.items() if s > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores = [s * 2 for s in scores.values()]
    print(f"Scores doubled: {doubled_scores}")

    active_players = [p for p in players if p in scores]
    print(f"Active players: {active_players}")

    print("=== Dict Comprehension Examples ===")

    player_scores = {p: s for p, s in scores.items()}
    print(f"Player scores: {player_scores}")

    score_categories = {
        "high": len([s for s in scores.values() if s >= 2100]),
        "medium": len([s for s in scores.values() if 1900 <= s < 2100]),
        "low": len([s for s in scores.values() if s < 1900])
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {p: len(a) for p, a in achievements.items()}
    print(f"Achievement counts: {achievement_counts}")

    print("=== Set Comprehension Examples ===")

    unique_players = {p for p in players}
    print(f"Unique players: {unique_players}")

    unique_achievements = {
        ach
        for ach_list in achievements.values()
        for ach in ach_list
    }
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {r for r in regions.values()}
    print(f"Active regions: {active_regions}")

    print("=== Combined Analysis ===")

    total_players = len(players)
    total_unique_achievements = len(unique_achievements)
    average_score = sum(scores.values()) / len(scores)

    max_score = max(scores.values())

    top_player = ""
    for player, score in scores.items():
        if score == max_score:
            top_player = player
            break

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score}")
    print(
        f"Top performer: {top_player} "
        f"({scores[top_player]} points, "
        f"{len(achievements[top_player])} achievements)"
    )


if __name__ == "__main__":
    main()

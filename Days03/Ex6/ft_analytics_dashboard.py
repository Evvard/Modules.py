def add_succes(achivment: set, nb_of_achivment: int,
               start_index: int = 0) -> set:
    tab = []
    count = 0
    added = 0

    for e in achivment:
        if count >= start_index and added < nb_of_achivment:
            tab += [e]
            added += 1
        count += 1
    return set(tab)


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    data = [('alice', 2300), ('bob', 1800), ('charlie', 2150), ('diana', 2050)]
    achivment_set = {'boss_slayer', 'collector', 'first_kill', 'level_10',
                     'perfectionist', 'speed_demon', 'treasure_hunter'}

    hight_score = [x for x, y in data if y > 2000]
    print(f"High scorers (>2000): {hight_score}")

    score_doubled = [(x * 2) for y, x in data]
    print(f"Scores doubled: {score_doubled}")

    active_player = [x for x, y in data if y != 2050]
    print(f"Active players: {active_player}\n")

    print("=== Dict Comprehension Examples ===")
    player_Score = {x: y for x, y in data}
    print(f"Player scores: {player_Score}")

    z = 0
    score_categories = {
        "hight": len([y for x, y in data if y > 2150]),
        "medium": len([y for x, y in data if y < 2151 and y > 2000]),
        "low": len([y for x, y in data if y < 2000])
        }
    print(f"Score categories: {score_categories}")

    Alice = add_succes(achivment_set, 5, 1)
    Bob = add_succes(achivment_set, 2, 4)
    Charlie = add_succes(achivment_set, 3, 3)
    Diana = add_succes(achivment_set, 1, 0)

    achievement_counts = {
        "alice": len([y for y in Alice]),
        "bob": len(([y for y in Bob])),
        "charlie": len(([y for y in Charlie])),
        "diana": len(([y for y in Diana]))
        }
    print(f"Achievement counts: {achievement_counts}\n")

    regions_data = [('alice', 'north'), ('bob', 'central'), ('charlie', 'north'), ('diana', 'east')]

    active_regions = {region for name, region in regions_data}
    player = {x for x in achievement_counts}
    print("=== Set Comprehension Examples ===")
    print(f"Unique players: {player}")

    all_player_achievements = [Alice, Bob, Charlie, Diana]
    unique_achievements = {achievement for player_set in all_player_achievements for achievement in player_set}
    print(f"Unique achievements: {unique_achievements}")

    regions_data = [('alice', 'north'), ('bob', 'central'), ('charlie', 'north'), ('diana', 'east')]
    active_regions = {region for name, region in regions_data}
    print(f"Active regions: {active_regions}")

    nb_player = len(achievement_counts)
    print("\n=== Combined Analysis ===")
    print(f"Total players: {nb_player}")
    print(f"Total unique achievements: {len(achivment_set)}")
    averge_score = (sum((x for y, x in data))) / nb_player
    print(f"Average score: {averge_score}")
    player = [x for y, x in data]
    max_score = max(player)
    player_max = {x for x, y in data if y == max_score}
    len_of_achivment =  len({x for x, y in data if y == max_score}) - 1
    print(f"Top performer: {player_max}, ({max_score}, {len_of_achivment})")

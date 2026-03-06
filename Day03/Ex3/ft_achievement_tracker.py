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


def occurence_cheker(search: set, name: set) -> int:
    i = 0
    for item in search:
        if item in name:
            i += 1
    return i


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    achivment_set = {'boss_slayer', 'collector', 'first_kill', 'level_10',
                     'perfectionist', 'speed_demon', 'treasure_hunter'}

    Alice = add_succes(achivment_set, 4, 3)
    print(f"Player alice achievements: {Alice}")
    Bob = add_succes(achivment_set, 4, 0)
    print(f"Player alice achievements: {Bob}")
    Charlie = add_succes(achivment_set, 5, 2)
    print(f"Player alice achievements: {Charlie}\n")

    print("=== Achievement Analytics ===")
    print(f"All unique achievements: {achivment_set}")
    print(f"Total unique achievements: {len(achivment_set)}\n")

    common = Alice.intersection(Bob)
    common = Charlie.intersection(common)
    print(f"Common to all players: {common}")
    rare_alice = Alice.difference(Bob).difference(Charlie)
    rare_bob = Bob.difference(Alice).difference(Charlie)
    rare_charlie = Charlie.difference(Alice).difference(Bob)
    rare_list = list(rare_alice) + list(rare_bob) + list(rare_charlie)
    rare = set(rare_list)
    i = occurence_cheker(rare, Alice) + occurence_cheker(rare, Bob)
    i += occurence_cheker(rare, Charlie)
    print(f"Rare achievements ({i} player): {rare}\n")

    print(f"Alice vs Bob common: {Alice.union(Bob)}")
    print(f"Alice unique: {Alice.difference(Bob)}")
    print(f"Bob unique: {Bob.difference(Alice)}")

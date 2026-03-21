from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    try:
        name = str('Fire Dragon')
        cost = int(5)
        rarity = str('Legendary')
        attack = int(7)
        health = int(5)
        mana = int(6)
        if mana < 0:
            raise Exception
    except Exception:
        print("Wrong value in input, retry")
        return

    print("Testing Abstract Base Class Design:\n")
    print("CreatureCard Info:")
    fire_dragon = CreatureCard(name, cost, rarity, attack, health)
    print(fire_dragon.get_card_info(), "\n", sep="")

    print(f"Playing Fire Dragon with {mana} mana available:")
    playable = fire_dragon.is_playable(mana)
    print(f"Playable: {playable}")
    if playable:
        game_state = {'mana_used': cost,
                      'effect': 'Creature summoned to battlefield'}
        play = fire_dragon.play(game_state)
        print(f"Play result: {play}")

        print("\nFire Dragon attacks Goblin Warrior:")
        target = {'target': 'Goblin Warrior',
                  'damage_dealt': 7, 'life_enemi': 6}
        result = fire_dragon.attack_target(target)
        print(f"Attack result: {result}")
    else:
        print(f"Playable: {fire_dragon.is_playable(mana)}")

    print(f"\nTesting insufficient mana ({mana - cost} available):")
    mana -= cost
    print(f"Playable: {fire_dragon.is_playable(mana)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()

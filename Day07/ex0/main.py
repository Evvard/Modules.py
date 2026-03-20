from CreatureCard import Card, CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    name = 'Fire Dragon'
    cost = 5
    rarity = 'Legendary'
    attack = 7
    health = 5

    mana_used = 5

    print("Testing Abstract Base Class Design:\n")
    print("CreatureCard Info:")
    fire_dragon = CreatureCard(name, cost, rarity, attack, health)
    print(fire_dragon.get_card_info(), "\n", sep="")

    mana = 6
    print(f"Playing Fire Dragon with {mana} mana available:")
    playable = fire_dragon.is_playable(mana)
    print(f"Playable: {playable}")
    if playable:
        game_state = {'mana_used': mana_used,
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

    print(f"\nTesting insufficient mana ({mana - mana_used} available):")
    mana -= mana_used
    print(f"Playable: {fire_dragon.is_playable(mana)}")

    print("\nAbstract pattern successfully demonstrated!")

if __name__ == "__main__":
    main()
from CreatureCard import Card, CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    name = 'Fire Dragon'
    cost = 5
    rarity = 'Legendary'

    tipe = {'type': 'Creature'}

    attack = 7
    health = 5

    fire_dragon = CreatureCard(name, cost, rarity, attack, health)




if __name__ == "__main__":
    main()

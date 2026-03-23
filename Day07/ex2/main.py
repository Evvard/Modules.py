from ex2.EliteCard import EliteCard


def main() -> None:
    print('\n=== DataDeck Ability System ===\n')

    print('EliteCard capabilities:')
    print('- Card: [\'play\', \'get_card_info\', \'is_playable\']')
    print('- Combatable: [\'attack\', \'defend\', \'get_combat_stats\']')
    print('- Magical: [\'cast_spell\', \'channel_mana\', \'get_magic_stats\']')
    print()

    data = {'name': 'Arcane Warrior', 'combat_type': 'melee', 'damage': 5,
            'mana_used': 4, 'life': '9'}
    elite_card = EliteCard()
    play = elite_card.play(data)
    if not play:
        return
    stat = elite_card.get_combat_stats()
    print('\n', stat['Action'], sep='')
    attack = elite_card.attack('Enemy')
    if not attack:
        return
    print(attack)
    defense = elite_card.defend(2)
    if not defense:
        return
    print(defense, "\n", sep='')
    stat = elite_card.get_magic_stats()
    print(stat['Action'])
    cast = elite_card.cast_spell('Fireball', ['Enemy1, Enemy2'])
    if not cast:
        return
    print(cast)
    mana_channell = elite_card.channel_mana(7)
    if not mana_channell:
        return
    print(mana_channell)

    print('\nMultiple interface implementation successful!')


if __name__ == '__main__':
    main()

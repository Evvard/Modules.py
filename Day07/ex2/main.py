from ex2.EliteCard import EliteCard


def main() -> None:
    print('\n=== DataDeck Ability System ===\n')

    print('EliteCard capabilities:')
    print('- Card: [\'play\', \'get_card_info\', \'is_playable\']')
    print('- Combatable: [\'attack\', \'defend\', \'get_combat_stats\']')
    print('- Magical: [\'cast_spell\', \'channel_mana\', \'get_magic_stats\']')
    print()

    data = {'name': 'Arcane Warrior', 'combat_type': 'melee', 'damage': 5,
            'mana_used': 4}
    elite_card = EliteCard()
    play = elite_card.play(data)
    if play == {}:
        return
    elite_card.get_combat_stats()






if __name__ == '__main__':
    main()

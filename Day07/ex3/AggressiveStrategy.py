from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex1.main import SpellCard, ArtifactCard


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        mana = 0
        lst = []
        damage = 0
        enemy = battlefield
        for card in hand:
            if isinstance(card, CreatureCard):
                damage += card.attack_damage
            elif isinstance(card, ArtifactCard) or isinstance(card, SpellCard):
                mana += card.cost
            lst += [card.name]
            if card.name in enemy:
                enemy.pop(card.name)

        result = {'cards_played': lst,
                  'mana_used': mana, 'targets_attacked': enemy,
                  'damage_dealt': damage}
        return result

    def get_strategy_name(self) -> str:
        return 'AggressiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        priority_list = []

        for target in available_targets:
            if target.lower() == "enemy player":
                priority_list.append(target)
                break
        for target in available_targets:
            if target.lower() != "enemy player":
                priority_list.append(target)
        return priority_list

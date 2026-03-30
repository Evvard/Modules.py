from ex0.Card import Card


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str = 'Commun',
                 effect_type: str = 'Cause damage to enemy'):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict = {}) -> dict:
        play_result = {'card_played': self.name, 'mana_used': self.cost,
                       'effect': self.effect_type}
        return play_result

    def resolve_effect(self, targets: list) -> dict:
        return {}

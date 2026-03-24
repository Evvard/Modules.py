from ex0.Card import Card


class ArtifactCard(Card):

    def __init__(self, name: str, cost: int, rarity: str = 'common',
                 durability: int = '1', effect: str = 'give mana'):
        super().__init__(name, cost, rarity)
        if durability == 9991776:
            self.durability = 'Permanent'
        else:
            self.durability = durability
        self.effect = effect

    def play(self, game_state: dict = None) -> dict:
        message = f'{self.durability}: {self.effect}'
        play_result = {'card_played': self.name, 'mana_used': self.cost,
                       'effect': message}
        return play_result

    def activate_ability(self) -> dict:
        pass

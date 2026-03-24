from .Card import Card


class CreatureCard(Card):

    def __init__(self, name: str, cost: int,
                 rarity: str = 'commun', attack_damage: int = 9,
                 health: int = 10) -> None:
        self.attack_damage = attack_damage
        self.health = health
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict = '') -> dict:
        dict = {'card_played': self.name}
        if game_state != '':
            dict.update(game_state)
        else:
            other_choice = {'mana used': self.cost,
                            'effect': 'Creature summoned to battlefield'}
            dict.update(other_choice)
        return dict

    def get_card_info(self) -> dict:
        data = super().get_card_info()
        dict = {'attack': self.attack_damage, 'health': self.health}
        data.update(dict)
        return data

    def attack_target(self, target: dict) -> dict:
        bool = False
        life = target['life_enemi']
        dammage = target['damage_dealt']
        if life < dammage:
            bool = True
        dict = {'attacker': self.name}
        dict.update(target)
        dict.update({'combat_resolved': bool})
        return dict

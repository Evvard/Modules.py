from .Card import Card


class CreatureCard(Card):

    def __init__(self, name: str, cost: int,
                 rarity: str = 'Commun', attack_damage: int = 9,
                 health: int = 10) -> None:
        self.attack_damage = attack_damage
        self.health = health
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict = '') -> dict:
        result = {'card_played': self.name}
        if game_state != '':
            result.update(game_state)
        else:
            other_choice = {'mana used': self.cost,
                            'effect': 'Creature summoned to battlefield'}
            result.update(other_choice)
        return result

    def get_card_info(self) -> dict:
        data = super().get_card_info()
        result = {'attack': self.attack_damage, 'health': self.health}
        data.update(result)
        return data

    def attack_target(self, target: dict) -> dict:
        bool = False
        try:
            life = target['life_enemi']
            dammage = target['damage_dealt']
            if life < dammage:
                bool = True
        except KeyError:
            print("No life and no dammage correct")
        resu = {'attacker': self.name}
        resu.update(target)
        resu.update({'combat_resolved': bool})
        return resu

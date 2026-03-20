from .Card import Card


class CreatureCard(Card):

    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        self.attack = attack
        self.health = health
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict) -> dict:
        dict = {'card_played': self.name}
        dict.update(game_state)
        return dict

    def get_card_info(self) -> dict:
        data = super().get_card_info()
        dict = {'attack': self.attack, 'health': self.health}
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

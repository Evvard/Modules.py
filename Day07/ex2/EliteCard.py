from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard (Card, Combatable, Magical):

    def __init__(self) -> None:
        pass

    def play(self, game_state: dict) -> dict:
        try:
            self.name = str(game_state['name'])
            self.combat_type = str(game_state['combat_type'])
            self.damage = int(game_state['damage'])
            self.mana = int(game_state['mana_used'])
            self.life = int(game_state['life'])
        except Exception or AttributeError or TypeError:
            print('Wrong Value in iput Stop the Program')
            return {}
        print(f'Playing {self.name} (Elite Card)')
        resu = {'card_played': self.name,
                'mana used': self.mana
                }
        return resu

    def get_card_info(self) -> dict:
        res = {'name': self.name, 'combat_type': self.combat_type,
               'damage': self.damage, 'mana': self.mana}
        return res

    def is_playable(self, available_mana: int) -> bool:
        if self.mana < available_mana:
            return False
        return True

    def attack(self, target: str = '') -> dict:
        try:
            if not target:
                raise TypeError
            str(target)
        except TypeError:
            print('Please Enter valid \'taget\' like in string format')
            return {}
        return {'attacker': self.name, 'target': target,
                'damage': self.damage, 'combat_type': self.combat_type}

    def defend(self, incoming_damage: int = None) -> dict:
        try:
            if not incoming_damage:
                raise TypeError
            int(incoming_damage)
        except TypeError:
            print('Please Enter valid \'incoming_damage\' like in int format')
            return {}
        if (self.life - incoming_damage) > 0:
            still_alive = True
        else:
            still_alive = False
        return {'defender': self.name, 'damage_taken': incoming_damage,
                'damage_blocked': (self.damage - incoming_damage),
                'still_alive': still_alive}

    def get_combat_stats(self) -> dict:
        return {'Action': 'Combat phase:'}

    def cast_spell(self, spell_name: str = '', targets: list = []) -> dict:
        try:
            if not spell_name or not targets:
                raise TypeError
            str(spell_name)
            list(targets)
        except TypeError:
            m = 'and \'target\' in list format !'
            print('Please Enter valid \'spell_name\' like in string format', m)
            return {}
        return {'caster': self.name, 'spell': spell_name,
                'targets': targets, 'mana_used': self.mana}

    def channel_mana(self, amount: int = None) -> dict:
        try:
            if (amount <= 0) or not amount:
                raise IndexError
            elif (amount < self.mana):
                raise ValueError
        except ValueError:
            print('You cheat bro, you use ability with not enought mana !')
        except IndexError:
            print('Negative value not accept !')
            return {}
        channeled = amount - self.mana
        return {'channeled': channeled, 'total_mana': amount}

    def get_magic_stats(self) -> dict:
        return {'Action': 'Magic phase:'}

from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str = "", cost: int = None,
                 rarity: str = "") -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        tipe = 'human'
        if 'Dragon' in self.name:
            tipe = 'Creature'
        dict = {'name': self.name, 'cost': self.cost}
        dict.update({'rarity': self.rarity})
        dict.update({'type': tipe})
        return dict

    def is_playable(self, available_mana: int) -> bool:
        if available_mana <= 3:
            return False
        return True
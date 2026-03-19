from abc import ABC, abstractmethod


class Card(ABC):

    def __init__(self, name: str = "", cost: int = "",
                 rarity: str = "") -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        tipe = 'human'
        if 'dragon' in self.name:
            tipe = 'Creature'
        {'name': self.name, 'cost': self.cost, 'rarity': self.rarity, 'type': tipe, 'attack': self.}

    def is_playable(self, available_mana: int) -> bool:
        if available_mana <= 3:
            return False
        return True

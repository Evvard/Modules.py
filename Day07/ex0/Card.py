from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    LEGENDARY = "Legendary"
    EPIC = "Epic"
    MYTHIC = "Mythic"
    RARE = "Rare"
    COMMON = "Common"


class Card(ABC):
    def __init__(self, name: str = "", cost: int = None,
                 rarity: str = "Common") -> None:
        self.name = name
        if cost < 0:
            print("---Negative value are not accept---")
            cost = -cost
        else:
            self.cost = cost
        valid_rarities = [r.value for r in Rarity]
        if rarity in valid_rarities:
            self.rarity = rarity
        else:
            message = "Game atribate you common rarity"
            print(f"The rarity value is not correctly define, {message}")
            self.rarity = "common"

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        tipe = 'Creature'
        if 'Human' in self.name or 'humain' in self.name:
            tipe = 'Human'
        dict = {'name': self.name, 'cost': self.cost}
        dict.update({'rarity': self.rarity})
        dict.update({'type': tipe})
        return dict

    def is_playable(self, available_mana: int) -> bool:
        if available_mana <= 3:
            return False
        return True

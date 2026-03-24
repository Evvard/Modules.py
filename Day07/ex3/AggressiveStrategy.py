from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex1.main import SpellCard, ArtifactCard

class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        mana = 0
        for card in hand:
            if isinstance(card, Card):
                damage += card.
            if isinstance(card, ArtifactCard) or isinstance(card, SpellCard):
                mana += card.mana

        result =  {'cards_played': ['Goblin Warrior', 'Lightning Bolt'],
                    'mana_used': mana, 'targets_attacked': ['Enemy Player'],
                    'damage_dealt': 8}

    def get_strategy_name(self) -> str:
        return 'AggressiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        pass


• Prioritizes attacking and dealing damage
• Plays low-cost creatures first for board presence
• Targets enemy creatures and player directly
• Returns comprehensive turn execution results
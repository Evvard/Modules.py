from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self.strategie_name = None
        self._factory = None
        self._strategy = None
        self.turn = 0
        self.damage = 0
        self.name = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        if not isinstance(factory, CardFactory):
            return
        if not isinstance(strategy, GameStrategy):
            return
        self.strategie_name = strategy.get_strategy_name()
        self._factory = factory
        self._strategy = strategy

    def simulate_turn(self) -> dict:
        deck = self._factory.create_themed_deck(3)
        hand = deck.get('creatures', []) + deck.get('spells', [])
        hand += deck.get('artifacts', [])

        ww = self._strategy.execute_turn(hand, ['Enemy Player'])
        self.name += len(ww['cards_played'])
        self.damage += int(ww['damage_dealt'])
        self.turn += 1
        return ww

    def get_engine_status(self) -> dict:
        return {
                'turns_simulated': self.turn,
                'strategy_used': self.strategie_name,
                'total_damage': self.damage,
                'cards_created': self.name
                }

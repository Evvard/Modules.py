from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self.strategie = None
        self.turn = 0
        self.damage = 0
        self.name = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        if not isinstance(factory, CardFactory):
            return
        elif not isinstance(strategy, GameStrategy):
            return
        self.strategie = strategy.get_strategy_name()
        self._factory = factory
        self._strategy = strategy

    def simulate_turn(self) -> dict:
        ww = self.strategie.execute_turn([], ['Enemy Player'])
        self.name = len(ww['cards_played'])
        self.damage += int(ww['damage_dealt'])
        self.turn += 1
        return {}

    def get_engine_status(self) -> dict:
        return {
                'turns_simulated': self.turn,
                'strategy_used': self.strategie,
                'total_damage': self.damage,
                'cards_created': self.name
                }

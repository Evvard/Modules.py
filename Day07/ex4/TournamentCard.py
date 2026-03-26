from ex0.Card import Card
from ex4.Rankable import Rankable
from ex2.Combatable import Combatable


class TournamentCard (Card, Combatable, Rankable):

    def __init__(self, name: str = "", cost: int = 1, rarity: str = "Common"):
        super().__init__(name, cost, rarity)
        self.reccord_player = [0, 0]
        self.reccord_ennemy = [0, 0]
        self.turn = 0
        self.total_card = 0

    def attack(self, target: str = 'Enemy') -> dict:
        ret = {'attaker': self.player1, 'target': self.player2}
        ret.update({'damage': self.damage1})
        return ret

    def defend(self, incoming_damage: int = 2) -> dict:
        self.damage2 = incoming_damage
        ret = {'attaker': self.player1, 'target': self.player2}
        ret.update({'damage': incoming_damage})

    def play(self, game_state: dict = {}) -> dict:
        self.player1 = game_state['player1']
        self.player2 = game_state['player2']
        self.damage1 = game_state['damage']
        self.rating_player = game_state['rating_player']
        self.rating_ennemy = game_state['rating_ennemy']
        self.total_card += 2
        attack = self.attack()
        defend = self.defend()
        self.turn += 1
        if defend == attack:
            pass
        return {}

    def calculate_rating(self) -> int:
        if self.damage1 < self.damage2:
            return 1
        return 0

    def get_rank_info(self) -> dict:
        i = self.calculate_rating()
        if i == 0:
            self.rating_ennemy -= 16
            self.rating_player += 16
            ret = {'winner_rating': self.rating_player}
            ret.update({'loser_rating': self.rating_ennemy})
        else:
            self.rating_player -= 16
            self.rating_ennemy += 16
            ret = {'winner_rating': self.rating_ennemy}
            ret.update({'loser_rating': self.rating_player})
        return ret

    def update_wins(self, wins: int) -> None:
        new_reccord = []
        if self.winner == self.player1:
            i = int(self.reccord_player[0])
            i += 1
            new_reccord = [i, self.reccord_player[1]]
            self.reccord_player = new_reccord
        else:
            i = int(self.reccord_ennemy[0])
            i += 1
            new_reccord = [i, self.reccord_ennemy[1]]
            self.reccord_ennemy = new_reccord

    def update_losses(self, losses: int) -> None:
        new_reccord = []
        if self.looser == self.player1:
            i = int(self.reccord_player[1])
            i += 1
            new_reccord = [self.reccord_player[1], i]
            self.reccord_player = new_reccord
        else:
            i = int(self.reccord_ennemy[1])
            i += 1
            new_reccord = [self.reccord_ennemy[0], i]
            self.reccord_ennemy = new_reccord

    def get_combat_stats(self) -> dict:
        result = self.damage1 - self.damage2
        if result < 0:
            self.winner = self.player2
            self.looser = self.player1
        else:
            self.winner = self.player1
            self.looser = self.player2
        self.update_wins(1)
        self.update_losses(1)
        rating = self.get_rank_info()
        res = {'winner': self.winner, 'loser': self.looser}
        res.update(rating)
        return res

    def get_tournament_stats(self) -> dict:
        me = f"({int(self.reccord_player[0])}"
        m = f"-{int(self.reccord_player[1])})"
        first = f"{self.player1} - \'Rating\': {self.rating_player}, {me}{m}"
        m = f"({int(self.reccord_ennemy[0])}-{int(self.reccord_ennemy[1])})"
        dos = f"{self.player2} - \'Rating\': {self.rating_ennemy}, {m}"

        tournament = {}
        if self.rating_ennemy > self.rating_player:
            tournament.update({'1.': dos, '2.': first})
        else:
            tournament.update({'1.': first, '2.': dos})
        result = {'total_cards': self.total_card, 'matches_played': self.turn}
        avg = (self.rating_ennemy + self.rating_player) / 2
        result.update({'avg_rating': avg})
        result.update({'platform_status': 'active'})
        tournament.update(result)
        return tournament

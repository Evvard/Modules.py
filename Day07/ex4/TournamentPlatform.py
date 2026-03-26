from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def register_card(self, card: TournamentCard) -> str:
        self.card = card

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if "dragon" in card1_id:
            player1 = 'Fire_dragon'
            damage = 5
        else:
            player1 = card1_id
            damage = 3
        if "wizard" in card2_id:
            player2 = "Ice Wizard"
        else:
            player2 = card2_id
        game_stat = {'player1': player1, 'player2': player2, 'damage': damage}
        game_stat.update({"rating_player": 1200})
        game_stat.update({"rating_ennemy": 1150})

        print(player1, f"(ID: {card1_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {int(game_stat['rating_player'])}")
        print("- Record: 0-0\n")
        print(player2, f"(ID: {card2_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {int(game_stat['rating_ennemy'])}")
        print("- Record: 0-0\n")
        print("Creating tournament match...")
        play = self.card.play(game_stat)
        if not play:
            pass
        stat = self.card.get_combat_stats()
        self.last = self.card.get_tournament_stats()
        return stat

    def get_leaderboard(self) -> list:
        print("\nTournament Leaderboard:")
        top = self.last.get('1.')
        losse = self.last.get('2.')
        return [top, losse]

    def generate_tournament_report(self) -> dict:
        print("\nPlatform Report:")
        result = {}
        card = self.last.get('total_cards')
        match = self.last.get('matches_played')
        avg = self.last.get('avg_rating')
        status = self.last.get('platform_status')
        result.update({'total_cards': card})
        result.update({'matches_played': match})
        result.update({'avg_rating': avg})
        result.update({'platform_status': status})
        return result

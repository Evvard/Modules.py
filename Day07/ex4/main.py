from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main() -> None:
    print('\n=== DataDeck Tournament Platform ===\n')
    print('Registering Tournament Cards...\n')
    card = TournamentCard()
    platform = TournamentPlatform()
    platform.register_card(card)
    stat = platform.create_match("dragon_001", "wizard_001")
    if not stat:
        return
    print("Match result:", stat)
    leaderboard = platform.get_leaderboard()
    for i in range(len(leaderboard)):
        print(f"{i + 1}.", leaderboard[i])
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == '__main__':
    main()

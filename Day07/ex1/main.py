from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")
    try:
        effect = 'Deal 3 damage to target'
        lightning_bolt = SpellCard("Lightning Bolt", 4.5, "Legendary", effect)
        mana_crystal = ArtifactCard('Mana Crystal', 5, "Mythic", 9991776,
                                    "+1 mana per turn")
        fire_dragon = CreatureCard('Fire Dragon', 5, "Common", 0, 4)
    except TypeError:
        print("The value in the input are not correct, please verify types.")
        return

    deck = Deck()
    deck.add_card(lightning_bolt)
    deck.add_card(mana_crystal)
    deck.add_card(fire_dragon)
    deck.shuffle()

    stat = deck.get_deck_stats()
    print("Building deck with different card types...")
    print(stat)
    print("\nDrawing and playing cards:\n")
    card = deck.draw_card()
    print(card.play(), '\n', sep='')
    card = deck.draw_card()
    print(card.play(), '\n', sep='')
    card = deck.draw_card()
    print(card.play(), '\n', sep='')

    print('Polymorphism in action: Same interface, different card behaviors!')


if __name__ == "__main__":
    main()

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")

    effect = 'Deal 3 damage to target'
    lightning_bolt = SpellCard("Lightning Bolt", 3, "Legendary", effect)

    mana_crystal = ArtifactCard('Mana Crystal', 2, "Mythic", 1776,
                                "+1 mana per turn")

    fire_dragon = CreatureCard('Fire Dragon', 5, "Common", 0, 4)

'effect': 'Creature summoned to battlefield'










if __name__ == "__main__":
    main()

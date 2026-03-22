from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard, Card
from random import shuffle


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def shuffle(self) -> None:
        shuffle(self.cards)

    def get_deck_stats(self) -> dict:
        creature = 0
        spell = 0
        artifacts = 0
        total_card = 0
        cost = 0
        for card in self.cards:
            if card:
                total_card += 1
                info = card.get_card_info()
                cost += info['cost']
                if isinstance(card, ArtifactCard):
                    artifacts += 1
                elif isinstance(card, SpellCard):
                    spell += 1
                elif isinstance(card, CreatureCard):
                    creature += 1
        try:
            cost = cost / total_card
            float(cost)
        except ZeroDivisionError:
            cost = 0
        result = {'total cards': total_card, 'creatures': creature,
                  'spells': spell, 'artifacts': artifacts, 'avg_cost':
                  cost}
        return result

    def remove_card(self, card_name: str) -> bool:
        for i in range(len(self.cards)):
            if self.cards[i].name == card_name:
                self.cards.pop(i)
                return True
        return False

    def draw_card(self) -> Card:
        for card in self.cards:
            rm = card.get_card_info()
            txt = ''
            if isinstance(card, ArtifactCard):
                txt = 'Artifacts'
            elif isinstance(card, SpellCard):
                txt = 'Spell'
            elif isinstance(card, CreatureCard):
                txt = 'Creature'
            print(f"Drew: {rm['name']} ({txt})")
            self.remove_card(rm['name'])
            return card

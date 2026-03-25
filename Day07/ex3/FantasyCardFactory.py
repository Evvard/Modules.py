from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard, Card
from ex1.main import SpellCard, ArtifactCard
import random


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if not name_or_power:
            nombre = random.randint(2, 4)
            return CreatureCard('goblin', nombre)
        try:
            name_or_power = int(name_or_power)
            if name_or_power <= 0:
                print("No negative Value, rebalancing of value")
                name_or_power = 2
            if name_or_power <= 4:
                return CreatureCard("goblin", name_or_power)
            if name_or_power > 4:
                return CreatureCard('dragon', name_or_power, 'Legendary')
        except ValueError or TypeError:
            pass
        try:
            str(name_or_power)
            if "dragon" in name_or_power.lower():
                nombre = random.randint(5, 8)
                return CreatureCard(name_or_power, nombre, "Legendary")
            elif "goblin" in name_or_power.lower():
                nombre = random.randint(2, 4)
                return CreatureCard(name_or_power, nombre)
            else:
                print("Wrong \'Name\' for Card, Game change to Goblin")
                nombre = random.randint(2, 4)
                return CreatureCard('name_or_power', nombre)
        except ValueError or TypeError:
            nombre = random.randint(2, 4)
            return CreatureCard('goblin', nombre, '')

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        spell = {'fire': 10, 'freeze': 5, "lightning": 3}
        if not name_or_power:
            return SpellCard('lightning Bolt', 7)
        try:
            for i in spell.keys():
                if str(i) in name_or_power.lower():
                    return SpellCard(name_or_power, int(spell[i]))
        except TypeError:
            pass
        try:
            name_or_power = int(name_or_power)
            if name_or_power <= 0:
                print("No negative Value, rebalancing of value")
                name_or_power = 3
            if name_or_power <= 3 and name_or_power > 0:
                return SpellCard("lightning Bolt", name_or_power)
            if name_or_power > 3 and name_or_power <= 5:
                return SpellCard("mega Freeze", name_or_power)
            if name_or_power > 5:
                return SpellCard("magic Fireball", name_or_power)
        except TypeError:
            return SpellCard('lightning Bolt', 7)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:

        if not name_or_power:
            return ArtifactCard('mana_ring', 2, durability=6)
        try:
            str(name_or_power)
            if 'mana' in name_or_power.lower():
                return ArtifactCard(name_or_power, 2)
            elif 'death' in name_or_power.lower():
                return ArtifactCard(name_or_power, 999, effect="kill enemy")
            else:
                return ArtifactCard(name_or_power, 5)
        except TypeError:
            pass
        try:
            name_or_power = int(name_or_power)
            if name_or_power <= 0:
                print("No negative Value, rebalancing of value")
                name_or_power = 3
            if name_or_power <= 3 and name_or_power > 0:
                return ArtifactCard("mana_ring", name_or_power)
            if name_or_power > 3 and name_or_power <= 5:
                return ArtifactCard('fire_ring', name_or_power)
            if name_or_power > 5:
                return ArtifactCard("heal_ring", name_or_power)
        except TypeError:
            return ArtifactCard('mana_ring', 7)

    def create_themed_deck(self, size: int) -> dict:
        deck = {"creatures": [], "spells": [], "artifacts": []}

        if size <= 0:
            return deck

        for _ in range(size):
            choice = random.choice(["creature", "spell", "artifact"])

            if choice == "creature":
                deck["creatures"].append(self.create_creature())
            elif choice == "spell":
                deck["spells"].append(self.create_spell())
            else:
                deck["artifacts"].append(self.create_artifact())
        return deck

    def get_supported_types(self) -> dict:
        return {
                'creatures': ['dragon', 'goblin'],
                'spells': ['fireball', 'freeze', 'lightning'],
                'artifacts': ['mana_ring', 'fire_ring', 'shield']
                }

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine
from ex0.CreatureCard import CreatureCard
from ex1.main import SpellCard





def main() -> None:

print("\n=== DataDeck Game Engine ===\n")

print("Configuring Fantasy Card Game...")



factory = FantasyCardFactory()

strategy = AggressiveStrategy()



engine = GameEngine()

print(f"Factory: {factory.__class__.__name__}")

print(f"Strategy: {strategy.get_strategy_name()}")



supported_types = {'creatures': ['dragon', 'goblin'],

'spells': ['fireball'],

'artifacts': ['mana_ring']}

print(f"Available types: {supported_types}\n")



hand = [

CreatureCard('Fire Dragon', 5, 'Common', 5, 10),

CreatureCard('Goblin Warrior', 2, 'Common', 3, 8),

SpellCard('Lightning Bolt', 3, 'Common', 'Deal 3 damage')

]



print("Simulating aggressive turn...")

print(f"Hand: {[f'{card.name} ({card.cost})' for card in hand]}")



turn_result = strategy.execute_turn(hand, ['Enemy Player'])

print("\nTurn execution:")

print(f"Strategy: {strategy.get_strategy_name()}")

print(f"Actions: {turn_result}")



engine.configure_engine(factory, strategy)

status = engine.get_engine_status()



print("\nGame Report:")

print(status)

message = 'Abstract Factory'

print(f"\n{message} + Strategy Pattern: Maximum flexibility achieved!")
from typing import Callable


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heals(target: str) -> str:
    return f"Heals {target}"


def base_spell(power: int) -> str:
    return f"Original: {power}"


def condition(spel: str, spell_power: int, power: int) -> bool:
    if power < spell_power:
        return True
    return False


def spell(spel: str, spell_power: int, power: int) -> str:
    return f"name = {spel}, power = {spell_power}"


def invisibility(power: int) -> str:
    return f"invisibility: {power}s"


def fire(power: int) -> str:
    return f"fire damage: {power}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str) -> tuple:
        return (spell1(target), spell2(target))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(power: int) -> str:
        return base_spell(power) + f" Amplified: {power * multiplier}"
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caste(spel: str, spell_power: int, power: int) -> str:
        if condition(spel, spell_power, power):
            return spell(spel, spell_power, power)
        return "Spell fizzled"
    return caste


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: int):
        new_list = []
        for spell in spells:
            new_list.append(spell(target))
        return new_list
    return sequence


def main() -> None:

    combined = spell_combiner(fireball, heals)
    print("Testing spell combiner...")
    print("Combined spell result:", combined("dragon"))
    print()
    print("Testing spell power amplifier...")
    amplifier = power_amplifier(base_spell, 3)
    print(amplifier(10))
    print()
    print("Testing spell conditional caster...")
    cast = conditional_caster(condition, spell)
    print(cast("Invisibility", 55, 5))
    print("test error")
    cast_error = conditional_caster(condition, spell)
    print(cast_error("Invisibility", 2, 5))

    print()
    sequence = spell_sequence([fire, invisibility])
    print("Testing spell sequence...")
    print(sequence(2))


if __name__ == "__main__":
    main()

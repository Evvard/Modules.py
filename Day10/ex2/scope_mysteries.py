from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def incrementation():
        nonlocal count
        count += 1
        return count
    return incrementation


def spell_accumulator(initial_power: int) -> Callable:
    accumulation_power = initial_power

    def accumulation(add_value: int):
        nonlocal accumulation_power
        accumulation_power += add_value
        return accumulation_power
    return accumulation

def enchantment_factory(enchantment_type: str) -> Callable:
    pass





if __name__ == "__main__":
    print("Testing mage counter...")
    a = mage_counter()
    for i in range(5):
        i += 1
        print(f"counter_a call {i}:", a())
    print()
    b = mage_counter()
    for i in range(5):
        i += 1
        print(f"counter_b call {i}:", b())
    print()
    print("Testing spell accumulator...")

    accumulator = spell_accumulator(100)
    print("Base 100, add 20:", accumulator(20))
    print("Base 100, add 30:", accumulator(30))
    print()
    print("Testing enchantment factory...")

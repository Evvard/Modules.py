from typing import Callable, Any


def mage_counter() -> Callable:
    count = 0

    def incrementation() -> int:
        nonlocal count
        count += 1
        return count
    return incrementation


def spell_accumulator(initial_power: int) -> Callable:
    accumulation_power = initial_power

    def accumulation(add_value: int) -> int:
        nonlocal accumulation_power
        accumulation_power += add_value
        return accumulation_power
    return accumulation


def enchantment_factory(enchantment_type: str) -> Callable:
    enchant = enchantment_type

    def items_enchant(items: str) -> str:
        return f"{enchant} {items}"
    return items_enchant


def memory_vault() -> dict[str, Callable]:
    secret = {}

    def store(key: str, value: Any) -> None:
        secret[key] = value

    def recall(key: str) -> Any:
        try:
            data = secret[key]
            return data
        except KeyError:
            return "Memory not found"

    return {"store": store, "recall": recall}


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
    enchant = enchantment_factory("Flaming")
    print(enchant("Sword"))
    enchant = enchantment_factory("Frozen")
    print(enchant("Shield"))
    print()
    print("Testing memory vault...")
    memory = memory_vault()
    memory['store']("secret", 42)
    memory['store']("gold", 42)
    print(memory['recall']('secret'))
    print(memory['recall']('g'))

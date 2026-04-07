from typing import Callable, Any
import functools
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    possibility = ["add", "multiply", "max", "min"]
    if not spells:
        return 0
    elif operation in possibility:
        if operation == possibility[0]:
            resultat = functools.reduce(add, spells)
        elif operation == possibility[1]:
            resultat = functools.reduce(mul, spells)
        elif operation == possibility[2]:
            resultat = functools.reduce(lambda x, y: max(x, y), spells)
        else:
            resultat = functools.reduce(lambda x, y: min(x, y), spells)
        return resultat
    return 0


def base_enchant(power: int, element: str, target: str) -> str:
    return f"power: {power}, element: {element}, target: {target}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    enchent: dict[str, Callable[..., Any]] = {
        "fart": functools.partial(base_enchantment, power=50, element="fart"),
        "air": functools.partial(base_enchantment, power=50, element="air"),
        "fire": functools.partial(base_enchantment, power=50, element="fire")
    }
    return enchent


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @functools.singledispatch
    def dispatcher(data: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(i: int) -> str:
        return f"Damage spell: {i} damage"

    @dispatcher.register(str)
    def _(i: str) -> str:
        return f"Enchantfireballment: {i}"

    @dispatcher.register(list)
    def _(i: list) -> str:
        return f"Multi-cast: {len(i)} spells"

    return dispatcher


def main() -> None:
    print()
    print("Testing spell reducer...")
    spells = [5, 3, 2, 1, 8]
    reducer = spell_reducer(spells, "add")
    print("add:", reducer)
    reducer = spell_reducer(spells, "ultiply")
    print("multipy:", reducer)
    reducer = spell_reducer(spells, "max")
    print("max:", reducer)
    reducer = spell_reducer(spells, "min")
    print("min:", reducer)
    print()
    enchanter = partial_enchanter(base_enchant)
    print("Testing partial enchanter...")
    print(enchanter["fart"](target="goblin"))
    print(enchanter["air"](target="women"))
    print(enchanter["fire"](target="human"))
    print()
    print("Testing memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))
    # print(memoized_fibonacci.cache_info())
    print()
    print("Testing spell dispatcher...")
    dispacher = spell_dispatcher()
    print(dispacher(42))
    print(dispacher("fireball"))
    print(dispacher(spells))
    print(dispacher({"key": "value"}))


if __name__ == "__main__":
    main()

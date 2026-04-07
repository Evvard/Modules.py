from typing import Callable, Any
import time
import functools


def spell_timer(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        temps = end - start
        print(f"Spell completed in {temps:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> Any:

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = args[2]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Any:

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            i = 1
            while i <= max_attempts:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    print(f"Spell failed, retrying... {i}/{max_attempts}")
                i += 1
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if (name.isalpha() or " ") and len(name) >= 3:
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:

    @spell_timer
    def power(name: str) -> str:
        time.sleep(0.101)
        return f"Result: {name} cast!"

    @power_validator(2)
    def power_test(e: str, name: str,  power: int) -> str:
        return f"{e}, power: {power}, name: {name}"

    @retry_spell(3)
    def fail():
        raise ValueError

    print("\nTesting spell timer..")
    print(power("ice"))
    print()
    print("Testing power validator")
    print(power_test("Try", "sword", 2))
    print()
    print("Testing power validator error")
    print(power_test("Try", "sword", 1))
    print()
    print("Testing Retry Spell")
    print(fail())
    print()
    print("Testing Static Methode")
    mage = MageGuild()
    name = " Test "
    err = "e"
    print(f"For {name}, validate_mage_name: {mage.validate_mage_name(name)}")
    print(f"For {err}, validate_mage_name: {mage.validate_mage_name(err)}")
    print()
    print(mage.cast_spell("oo", 88))


if __name__ == "__main__":
    main()

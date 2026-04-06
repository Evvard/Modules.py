from functools import wraps
from typing import Callable


def spell_timer(func: Callable) -> Callable:


def power_validator(min_power: int) -> Callable:

def retry_spell(max_attempts: int) -> Callable:





class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not len(name) >= 3 or not name.isalpha():
            return False
        return True


    def cast_spell(self, spell_name: str, power: int) -> str:

        return f"Successfully cast {spell_name} with {power} power"
        return "Insufficient power for this spell"

def main() -> None:
    print("Testing spell timer..")




if __name__ == "__main__":
    main()

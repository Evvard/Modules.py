import alchemy.elements
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal

from alchemy.elements import create_earth, create_fire
from alchemy.potions import strength_potion


def main() -> None:
    print("=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    module_import = alchemy.elements.create_fire()
    print(f"alchemy.elements.create_fire(): {module_import}\n")

    print("Method 2 - Specific function import:")
    specific_import = create_water()
    print(f"create_water(): {specific_import}\n")

    print("Method 3 - Aliased import:")
    aliased_import = heal()
    print(f"heal(): {aliased_import}\n")

    print("Method 4 - Multiple imports")

    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion: {strength_potion()}\n")

    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()

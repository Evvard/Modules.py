from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell


def late_import() -> None:
    from alchemy.grimoire.spellbook import record_spell as r_s
    print("Testing late import technique:")
    message = r_s("Lightning", "air")
    print(f"record_spell(\"Lightning\", \"air\"): {message}")


def main() -> None:
    print("=== Circular Curse Breaking ===\n")
    print("Testing ingredient validation:")
    message = validate_ingredients("fire air")
    print(f"validate_ingredients(\"fire air\"): {message}")
    message = validate_ingredients("dragon scales")
    print(f"validate_ingredients(\"dragon scales\"): {message}")

    print("\nTesting spell recording with validation:")
    message = record_spell("Fireball", "fire air")
    print(f"record_spell(\"Fireball\", \"fire air\"): {message}")
    message = record_spell("Dark Magic", "shadow")
    print(f"record_spell(\"Dark Magic\", \"shadow\"): {message}\n")

    late_import()

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()

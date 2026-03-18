from alchemy.grimoire.validator import validate_ingredients


def record_spell(spell_name: str = "", ingredients: str = "") -> str:
    validate = validate_ingredients(ingredients)
    if "VALID" in validate:
        return f"Spell recorded: {spell_name} ({validate})"
    return f"Spell rejected: {spell_name} ({validate})"

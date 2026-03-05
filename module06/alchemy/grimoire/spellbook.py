def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    validation = validate_ingredients(ingredients)
    output = 'Spell '
    output += ('rejected: ' if 'INVALID' in validation else 'recorded: ')
    output += f'{spell_name} ({validation})'

    return output

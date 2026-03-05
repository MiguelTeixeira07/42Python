def validate_ingredients(ingredients: str) -> str:
    keywords = {
        'fire',
        'water',
        'earth',
        'air'
    }
    valid = False

    for word in keywords:
        if word in ingredients:
            valid = True

    return f'{ingredients} - {"VALID" if valid else "INVALID"}'

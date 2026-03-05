from .elements import create_fire, create_water, create_earth, create_air


def healing_potion() -> str:
    return f'Healing potion brewed with {create_water()} and {create_fire()}'


def strength_potion() -> str:
    return f'Strength potion brewed with {create_earth()} and {create_fire()}'


def ivisibility_potion() -> str:
    out = 'Invisibility potion brewed with '
    out += f'{create_air()} and {create_water()}'
    return out


def wisdom_potion() -> str:
    out = 'Wisdom potion brewed with all elements: '
    out += f'{create_earth()} {create_fire()} {create_water()} {create_air()}'
    return out

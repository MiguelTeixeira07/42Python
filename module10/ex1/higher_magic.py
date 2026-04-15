from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner(*args, **kwargs) -> tuple[str, str]:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))

    return combiner


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args, **kwargs) -> int:
        return base_spell(*args, **kwargs) * multiplier

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(*args, **kwargs) -> str:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return 'Spell fizzled'

    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast(*args, **kwargs) -> list[str]:
        return [spell(*args, **kwargs) for spell in spells]

    return cast


def main() -> None:
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def damage_check(target: str) -> bool:
        return target[0] == 'M'

    def lightning(target: str) -> str:
        return f"Lightning strikes {target}"

    def base_damage() -> int:
        return 67

    target = 'Dragon'

    print('=== Spell Combiner ===')
    combined = spell_combiner(fireball, lightning)
    print(*(result for result in combined(target)), sep=' | ')

    print('\n=== Power Amplifier ===')
    print(f'Original: {base_damage()}')
    amplified = power_amplifier(base_damage, 3)
    print(f'Amplified: {amplified()}')

    print("\n=== Conditional Cast (casts if target starts with 'M') ===")
    conditional = conditional_caster(damage_check, fireball)
    print(f'Target = "{target}": {conditional(target)}')
    target = 'Mouse'
    print(f'Target = "{target}": {conditional(target)}')

    print('\n=== Spell Sequence ===')
    spells = [fireball, heal, lightning]
    sequence = spell_sequence(spells)
    print(*(sequence(target)), sep=' | ')


if __name__ == '__main__':
    main()

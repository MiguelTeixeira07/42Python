from collections.abc import Callable
from time import perf_counter, sleep
from functools import wraps
from typing import Any


def spell_timer(spell: Callable) -> Callable:
    @wraps(spell)
    def wrapper(*args, **kwargs) -> Any:
        print(f'Casting {spell.__name__}...')
        start = perf_counter()
        result = spell(*args, **kwargs)
        end = perf_counter()
        print(f'Spell completed in {end - start:.3f} seconds')

        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(spell: Callable) -> Callable:
        @wraps(spell)
        def wrapper(*args, **kwargs) -> Any:
            power = args[2]
            if power >= min_power:
                return spell(*args, **kwargs)

            return 'Insuficient power for this spell'

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(spell: Callable) -> Callable:
        @wraps(spell)
        def wrapper(*args, **kwargs) -> Any:
            failed = 0
            failed_msg = f'Spell failed after {max_attempts} attempts'

            for i in range(max_attempts):
                try:
                    result = spell(*args, **kwargs)
                except Exception:
                    print('Spell failed, retrying... '
                          f'(attempt {i}/{max_attempts})')
                    failed += 1

            return result if failed != max_attempts else failed_msg

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) > 2 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        sleep(0.101)
        return f'Successfully cast {spell_name} with {power} power'


def main() -> None:
    print('=== Spell Timer ===')
    mage = MageGuild()
    print(spell_timer(mage.cast_spell)('Fireball', 11))

    print('\n=== Power Validator ===')
    print('5 power:', mage.cast_spell('Fireball', 5))
    print('15 power:', mage.cast_spell('Fireball', 15))

    print('\n=== Retry Spell ===')
    print('Invalid:')
    print(retry_spell(3)(mage.cast_spell)('Fireball', '5'))
    print('Valid:')
    print(retry_spell(3)(mage.cast_spell)('Fireball', 15))

    print('\n=== Mage Name Validation ===')
    name = 'John'
    print(f'{name} is a {"V" if mage.validate_mage_name(name) else "Inv"}alid'
          ' name')
    name = 'b5'
    print(f'{name} is a {"V" if mage.validate_mage_name(name) else "Inv"}alid'
          ' name')


if __name__ == '__main__':
    main()

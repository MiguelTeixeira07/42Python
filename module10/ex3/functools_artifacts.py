from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min
    }

    try:
        op = operations[operation]
    except KeyError:
        raise ValueError(f'Invalid operation: "{operation}"')

    return reduce(op, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'Fire': partial(base_enchantment, 50, 'Fire'),
        'Freeze': partial(base_enchantment, 50, 'Freeze'),
        'Earth': partial(base_enchantment, 50, 'Earth')
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def base_spell(spell: Any) -> str:
        return 'Unknown spell type'

    @base_spell.register(int)
    def _1(damage: int) -> str:
        return f'Damage spell: {damage} damage'

    @base_spell.register(str)
    def _2(enchant: str) -> str:
        return f'Enchantment: {enchant}'

    @base_spell.register(list)
    def _3(spells: list) -> str:
        return f'Multi-cast: {len(spells)} spells'

    return base_spell


def main() -> None:
    print('=== Spell Reducer ===')
    spells = [34, 67, 76, 43]
    print('Sum:', spell_reducer(spells, 'add'))
    print('Multiply:', spell_reducer(spells, 'multiply'))
    print('Max:', spell_reducer(spells, 'max'))
    print('Min:', spell_reducer(spells, 'min'))

    print('\n=== Partial Enchanter ===')
    enchants = ['Fire', 'Freeze', 'Earth']
    e = partial_enchanter(lambda p, e, t: f'Enchanted {t} with {e} (pow={p})')
    print(*(e[enchant]('Sword') for enchant in enchants), sep='\n')

    print('\n=== Memoized Fibonacci ===')
    print('Fib(0):', memoized_fibonacci(0))
    print('Fib(1):', memoized_fibonacci(1))
    print('Fib(10):', memoized_fibonacci(10))
    print('Fib(15):', memoized_fibonacci(15))

    print('\n=== Spell Dispatcher ===')
    types = (42, 'fireball', [1, 2, 3], lambda x: x)
    spell = spell_dispatcher()
    print(*(spell(t) for t in types), sep='\n')


if __name__ == '__main__':
    main()

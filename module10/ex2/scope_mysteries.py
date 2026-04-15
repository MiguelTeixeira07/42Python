from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    def counter_function() -> int:
        counter_function.count += 1
        return counter_function.count

    counter_function.count = 0

    return counter_function


def spell_accumulator(initial_power: int) -> Callable:
    def accumulator(power: int) -> int:
        accumulator.total_power += power
        return accumulator.total_power

    accumulator.total_power = initial_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def generator(item: str) -> str:
        return f'{enchantment_type} {item}'

    return generator


def memory_vault() -> dict[str, Callable]:
    data = {}

    def store(key: str, value: Any) -> None:
        data.update({key: value})

    def recall(key: str) -> Any:
        if key in data:
            return data[key]
        return 'Memory not found'

    return {'store': store, 'recall': recall}


def main() -> None:
    print('=== Mage Counter ===')
    counter_a = mage_counter()
    print('counter_a call 1:', counter_a())
    print('counter_a call 2:', counter_a())
    counter_b = mage_counter()
    print('counter_b call 1:', counter_b())

    print('\n=== Spell Accumulator ===')
    accumulator = spell_accumulator(100)
    print('Base 100, add 20', accumulator(20))
    print('Base 100, add 30', accumulator(30))

    print('\n=== Enchantment Factory ===')
    enchant = enchantment_factory('Flaming')
    print(enchant('Sword'))
    enchant = enchantment_factory('Frozen')
    print(enchant('Shield'))

    print('\n=== Memory Vault ===')
    key = 'secret'
    value = 42
    print(f"Store '{key}' = {value}")
    vault = memory_vault()
    vault['store'](key, value)
    print(f"Recall '{key}': {vault['recall'](key)}")
    key = 'unknown'
    print(f"Recall '{key}': {vault['recall'](key)}")


if __name__ == '__main__':
    main()

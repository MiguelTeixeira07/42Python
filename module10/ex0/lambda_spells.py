def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '* ' + x + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    ma = max(mages, key=lambda x: x['power'])
    mi = min(mages, key=lambda x: x['power'])
    av = round(sum(m['power'] for m in mages) / len(mages), 2)

    return {
        'max_power': ma['power'], 'min_power': mi['power'], 'avg_power': av
    }


def main() -> None:
    try:
        from data_generator import FuncMageDataGenerator as gen
    except ModuleNotFoundError:
        artifacts = [
            {'name': 'Crystal Orb', 'power': 87, 'type': 'accessory'},
            {'name': 'Water Chalice', 'power': 70, 'type': 'armor'},
            {'name': 'Crystal Orb', 'power': 101, 'type': 'weapon'},
            {'name': 'Lightning Rod', 'power': 85, 'type': 'weapon'},
            {'name': 'Ice Wand', 'power': 108, 'type': 'focus'}
        ]

        mages = [
            {'name': 'Rowan', 'power': 95, 'element': 'light'},
            {'name': 'Jordan', 'power': 60, 'element': 'ice'},
            {'name': 'Ember', 'power': 83, 'element': 'water'},
            {'name': 'Rowan', 'power': 92, 'element': 'light'},
            {'name': 'Ash', 'power': 84, 'element': 'light'}
        ]

        spells = [
            'tornado',
            'darkness',
            'heal',
            'fireball',
            'blizzard',
            'earthquake'
        ]
    else:
        artifacts = gen.generate_artifacts()
        mages = gen.generate_mages()
        spells = gen.generate_spells()

    print('Artifacts:')
    for artifact in artifacts:
        print(*(f'{key}:\t{val}' for key, val in artifact.items()), sep=',\t')
    print()
    print('Sorted Artifacts:')
    for artifact in artifact_sorter(artifacts):
        print(*(f'{key}:\t{val}' for key, val in artifact.items()), sep=',\t')

    print('\n=======================================\n')

    print('Mages:')
    for mage in mages:
        print(*(f'{key}:\t{val}' for key, val in mage.items()), sep=',\t')
    print()
    print('Filtered Mages (min=75):')
    for mage in power_filter(mages, 75):
        print(*(f'{key}:\t{val}' for key, val in mage.items()), sep=',\t')

    print('\n=======================================\n')

    print('Spells:')
    print(*(spell for spell in spells), sep=', ')
    print()
    print('Transformed Spells:')
    print(*(spell for spell in spell_transformer(spells)))

    print('\n=======================================\n')

    print('Mage Stats:')
    print(*(f'{k}: {v}' for k, v in mage_stats(mages).items()), sep=', ')


if __name__ == '__main__':
    main()

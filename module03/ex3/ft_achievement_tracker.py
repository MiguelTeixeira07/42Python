import random


def gen_player_achievements() -> set:
    achievements = {
        'First Steps',
        'Speed Runner',
        'Survivor',
        'Treasure Hunter',
        'Master Explorer',
        'Collector Supreme',
        'Sharp Mind',
        'Strategist',
        'Boss Slayer',
        'World Savior',
        'Untouchable',
        'Unstoppable',
        'Hidden Path Finder',
    }

    achievements_list = []
    for achievement in achievements:
        achievements_list.append(achievement)

    amount = random.randint(5, len(achievements_list))
    player_achievements = set()

    while len(player_achievements) < amount:
        player_achievements.add(
            achievements_list[random.randint(0, len(achievements_list) - 1)]
        )
    return player_achievements


def main() -> None:
    print('=== Achievement Tracker System ===\n')

    player_names = ['Alice', 'Bob', 'Charlie', 'Dylan']
    player_sets = {}

    for name in player_names:
        player_sets[name] = gen_player_achievements()
        print(f'Player {name}: {player_sets[name]}\n')

    all_distinct = set()
    for name in player_names:
        all_distinct = all_distinct.union(player_sets[name])
    print(f'All distinct achievements: {all_distinct}\n')

    common = player_sets[player_names[0]]
    for name in player_names[1:]:
        common = common.intersection(player_sets[name])
    print(f'Common achievements: {common}\n')

    for name in player_names:
        others = set()

        for other_name in player_names:
            if other_name != name:
                others = others.union(player_sets[other_name])

        only_this_player = player_sets[name].difference(others)
        print(f'Only {name} has: {only_this_player}\n')

    for name in player_names:
        missing = all_distinct.difference(player_sets[name])
        print(f'{name} is missing: {missing}')


if __name__ == '__main__':
    main()

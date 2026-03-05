from ex0.CreatureCard import CreatureCard


def main():
    print("\n=== DataDeck Card Foundation ===\n")

    print('Testing Abstract Base Class Design:\n')

    dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    goblin_warrior = CreatureCard('Goblin Warrior', 3, 'Uncommon', 2, 1)

    dragon_info = dragon.get_card_info()

    print('CreatureCard info:')
    print(dragon_info)

    print(f'\nPlaying {dragon_info['name']} with 6 mana available:')
    result = dragon.play({"player_mana": 6,
                          "battlefield": [],
                          "graveyard": [],
                          "player_health": 20,
                          "enemy_health": 20})
    print(result)

    print('\nFire Dragon attacks Goblin Warrior:')
    attack = dragon.attack_target(goblin_warrior)
    print(f'Attack result: {attack}')

    playable = dragon.is_playable(3)
    print('\nTesting insufficient mana (3 available): ', end='')
    print(f'Playable: {"True" if playable else "False"}')


if __name__ == "__main__":
    main()

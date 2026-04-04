from .CreatureCard import CreatureCard


def main():
    print("\n=== DataDeck Card Foundation ===\n")

    print('Testing Abstract Base Class Design:\n')

    dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
    goblin_warrior = CreatureCard('Goblin Warrior', 3, 'Uncommon', 2, 1)

    game_state = {
        "player_mana": 6,
        "battlefield": [goblin_warrior],
        "graveyard": [],
        "player_health": 20,
        "enemy_health": 20
    }

    dragon_info = dragon.get_card_info()

    print('CreatureCard info:')
    print(dragon_info)

    game_state = dragon.play(game_state)

    game_state = dragon.attack_target(goblin_warrior, game_state)

    print('\nTesting insufficient mana ', end='')
    print(f'({game_state["player_mana"]} available):')
    dragon.play(game_state)

    print('\nAbstract pattern successfully demonstrated!')


if __name__ == "__main__":
    main()

from ex2.EliteCard import EliteCard


def main():

    print("\n=== DataDeck Ability System ===\n")

    warrior = EliteCard("Arcane Warrior", 4, "Epic", 5, 3, 4)

    game_state = {"player_mana": 10}

    print("EliteCard capabilities:")
    print("- Card:", ["play", "get_card_info", "is_playable"])
    print("- Combatable:", ["attack", "defend", "get_combat_stats"])
    print("- Magical:", ["cast_spell", "channel_mana", "get_magic_stats"])

    print("\nPlaying Arcane Warrior (Elite Card):")
    warrior.play(game_state)

    print("\nCombat phase:")
    warrior.attack("Enemy")
    warrior.defend(5)

    print("\nMagic phase:")
    warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    warrior.channel_mana(3)

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()

def water_plants(plant_list: list) -> None:
    possible_plants = ("Cactus", "Rose", "Tulip", "Oak", "Sunflower")
    print("= Watering System =")
    try:
        for plant in plant_list:
            if not (plant in possible_plants):
                raise ValueError(f"Error: Cannot water {plant}!")
            print(f"watering {plant}...")
    except ValueError as e:
        print(e)
        return
    finally:
        print("Cleaning watering system up")


def test_watering_system() -> None:
    good_plants = ["Rose", "Sunflower", "Cactus", "Tulip", "Oak"]
    bad_plants = ["Rose", "Sunflower", "Cactus", "Orchid", "Oak"]

    print("=== Watering with good plant list ===")
    water_plants(good_plants)
    print()
    print("=== Watering with bad plant list ===")
    water_plants(bad_plants)
    print()
    print("Cleanup always happens, even with errors!")

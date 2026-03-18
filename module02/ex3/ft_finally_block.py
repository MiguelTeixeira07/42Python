def water_plants(plant_list: list) -> None:
    possible_plants = ("tomato", "lettuce", "carrots")
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not (plant in possible_plants):
                raise ValueError(f"Error: Cannot water {plant}!")
            print(f"watering {plant}...")
    except ValueError as e:
        print(f"{e} - invalid plant!")
        return
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    good_plants = ["tomato", "lettuce", "carrots"]
    bad_plants = ["tomato", None, "lettuce", "carrots"]

    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(good_plants)
    print("Watering completed successfully!")

    print("\nTesting with error...")
    water_plants(bad_plants)
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == '__main__':
    test_watering_system()

def check_plant_health(plant_name, water_level, sunlight_hours):
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high")

    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")

    try:
        print("Testing good values...")
        print(check_plant_health("tomato", 5, 6))
    except ValueError as e:
        print("Error:", e)

    try:
        print("Testing empty plant name...")
        check_plant_health("", 5, 6)
    except ValueError as e:
        print("Error:", e)

    try:
        print("Testing bad water level...")
        check_plant_health("tomato", 15, 6)
    except ValueError as e:
        print("Error:", e)

    try:
        print("Testing bad sunlight hours...")
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print("Error:", e)

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()

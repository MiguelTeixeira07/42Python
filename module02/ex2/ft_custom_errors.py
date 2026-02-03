class GardenError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message) -> None:
        super().__init__(message)


def test_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def test_water() -> None:
    raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        test_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        test_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")
    for func in (test_plant, test_water):
        try:
            func()
        except GardenError as e:
            print(f"Caught a garden error: {e}")
        print()
    print("All custom error types work correctly!")

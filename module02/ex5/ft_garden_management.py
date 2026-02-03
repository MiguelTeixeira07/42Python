class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = {}

    def add_plant(self, name, water, sun):
        if not name:
            raise PlantError("Plant name cannot be empty!")

        if water < 1 or water > 10:
            raise PlantError(f"Water level {water} is too high (max 10)")

        if sun < 2 or sun > 12:
            raise PlantError(f"Sunlight hours {sun} is too low (min 2)")

        self.plants[name] = {"water": water, "sun": sun}

    def water_plants(self):
        print("Opening watering system")
        try:
            if not self.plants:
                raise GardenError("Not enough water in tank")

            for plant in self.plants:
                print(f"Watering {plant} - success")

        except GardenError:
            raise

        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, name):
        if name not in self.plants:
            raise PlantError(f"Plant '{name}' does not exist")

        p = self.plants[name]

        if p["water"] < 1 or p["water"] > 10:
            raise ValueError(f"Water level {p['water']} is too high (max 10)")

        if p["sun"] < 2 or p["sun"] > 12:
            raise ValueError(f"Sunlight hours {p['sun']} is too low (min 2)")

        return f"{name}: healthy (water: {p['water']}, sun: {p['sun']})"


def test_garden_management():
    print("=== Garden Management System ===")
    garden = GardenManager()

    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
        print("Added tomato successfully")

        garden.add_plant("lettuce", 15, 6)
        print("Added lettuce successfully")

    except PlantError as e:
        print("Error adding plant:", e)

    print("Watering plants...")
    try:
        garden.water_plants()
    except GardenError as e:
        print("Caught GardenError:", e)

    print("Checking plant health...")
    try:
        print(garden.check_health("tomato"))
        print(garden.check_health("lettuce"))
    except (PlantError, ValueError) as e:
        print("Error checking lettuce:", e)

    print("Testing error recovery...")
    try:
        empty = GardenManager()
        empty.water_plants()
    except GardenError as e:
        print("Caught GardenError:", e)
        print("System recovered and continuing...")

    print("Garden management system test complete!")

class Plant:
    """This class represents a plant"""

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        print(f"Created: {self.name} ({self.height}cm, {self.age})")

    def get_info(self):
        """This method outputs all the information about your plants"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plants = []
    names = ("Rose", "Tulip", "Sunflower", "Cactus", "Oak tree")
    heights = (30, 25, 80, 120, 435)
    ages = (25, 20, 50, 365, 10500)

    for i in range(5):
        plants.append(Plant(names[i], heights[i], ages[i]))

    print("\n=== Your Plants ===")
    for i in range(5):
        plants[i].get_info()

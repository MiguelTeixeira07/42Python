class Plant:
    """Generic plant."""

    def __init__(self, name: str, height: int, age: int):
        """Create a plant with name, height and age."""
        self.name = name
        self.height = height
        self.age = age

    def show_data(self):
        """Print basic plant information."""
        print(f"{self.name} ({self.__class__.__name__}): "
              f"{self.height}cm, {self.age} days")


class Flower(Plant):
    """Flower plant."""

    def __init__(self, name, height, age, color: str):
        """Create a flower with a color."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Print a blooming message."""
        print(f"{self.name} is blooming beautifully!")

    def show_data(self):
        """Print plant data and flower color."""
        super().show_data()
        print(f"{self.color} color")


class Tree(Plant):
    """Tree plant."""

    def __init__(self, name, height, age, trunk_diameter: int):
        """Create a tree with trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """Calculate and print shade area."""
        shade_area = self.trunk_diameter // 10 * self.height
        print(f"{self.name} provides {shade_area} square meters of shade")

    def show_data(self):
        """Print plant data and shade produced."""
        super().show_data()
        self.produce_shade()


class Vegetable(Plant):
    """Vegetable plant."""

    def __init__(self, name, height, age, harv_season: str, nutri_value: str):
        """Create a vegetable with season and nutrition info."""
        super().__init__(name, height, age)
        self.harv_season = harv_season
        self.nutri_value = nutri_value

    def show_data(self):
        """Print plant data, season and nutrition."""
        super().show_data()
        print(f"{self.harv_season}")
        print(f"{self.name} is {self.nutri_value}")


if __name__ == "__main__":
    """Run demo with different plant types."""
    plants = [
        Plant("Cactus", 120, 365),
        Plant("Weeds", 15, 365),
        Flower("Rose", 30, 25, "white"),
        Flower("Tulip", 25, 20, "orange"),
        Tree("Eucaliptus", 1100, 5*365, 3),
        Tree("Cork Oak", 800, 27*365, 7),
        Vegetable("Eggplant", 160, 50, "march to june", "rich in fiber"),
        Vegetable("Cabbage", 30, 40, "february to may", "rich in folate"),
    ]

    print("=== Garden Plant Types ===\n")
    for plant in plants:
        plant.show_data()
        print()

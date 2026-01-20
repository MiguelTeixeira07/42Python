class Plant:
    """This class represents a plant"""

    def __init__(self, name: str, height: int, age_d: int):
        self.name = name
        self.height = height
        self.age_d = age_d
        self.growth: int = 0

    def grow(self):
        """This method simulates the growth in height of your plant"""
        self.growth += self.height // 10
        self.height += self.height // 10
        return self

    def age(self):
        """This method simulates the aging of your plant"""
        self.age_d += 1
        self.grow()
        return self

    def get_info(self):
        """This method outputs all the information about your plants"""
        print(f"{self.name}: {self.height}cm, {self.age_d} days old")
        if self.growth:
            print(f"Growth this week: +{self.growth}\n")


if __name__ == "__main__":
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Tulip", 20, 15)
    plant_3 = Plant("Sunflower", 80, 50)

    print("\n=== Day 1 ===")
    plant_1.get_info()
    plant_2.get_info()
    plant_3.get_info()

    for i in range(7):
        plant_1.age()
        plant_2.age()
        plant_3.age()

    print("\n=== Day 7 ===")
    plant_1.get_info()
    plant_2.get_info()
    plant_3.get_info()

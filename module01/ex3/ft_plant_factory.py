class Plant:
    """This class represents a plant"""

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.growth: int = 0
        print(f"Created: {self.name} ({self.height}cm, {self.age})\n")

    def get_info(self):
        """This method outputs all the information about your plants"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plants = [0, 0, 0, 0, 0]

    for i in range(5):
        print(f"=== Enter Plant {i + 1} Info ===")
        name = input("Name: ")
        height = int(input("Height: "))
        age = int(input("Age: "))
        plants[i] = Plant(name, height, age)

    print("\n=== Your Plants ===")
    for i in range(5):
        plants[i].get_info()

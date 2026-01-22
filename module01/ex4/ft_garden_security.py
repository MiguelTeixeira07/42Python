class SecurePlant:
    """This class represents a plant"""

    def __init__(self, name: str):
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Created: {self.name}")

    def set_height(self, height):
        try:
            if height >= 0:
                self.__height = height
                print(f"Height updated to: {self.__height}")
            else:
                print("Could not update height: Negative number")
        except TypeError:
            print("Could not update height: Invalid input")

    def set_age(self, age):
        try:
            if age >= 0:
                self.__age = age
                print(f"Age updated to: {self.__age}")
            else:
                print("Could not update age: Invalid input")
        except TypeError:
            print("Could not update age: Invalid input")

    def get_info(self):
        """This method outputs all the information about your plants"""
        print(f"{self.name}: {self.__height}cm, {self.__age} days old")


if __name__ == "__main__":
    plants = []
    names = ("Rose", "Tulip", "Sunflower", "Cactus", "Oak tree")
    heights = (30, 25, -80, 120, 435)
    ages = (25, 20, 50, 365, "10500")

    print("=== Welcome to My Garden ===")
    for i in range(5):
        plants.append(SecurePlant(names[i]))
    print()
    for i in range(5):
        plants[i].set_height(heights[i])
        plants[i].set_age(ages[i])
        print()

    print("\n=== Your Plants ===")
    for i in range(5):
        plants[i].get_info()

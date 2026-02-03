class Plant:
    """This class represents a plant"""
    name: str
    height: int
    age: int


if __name__ == "__main__":
    plant_1 = Plant()
    plant_2 = Plant()
    plant_3 = Plant()

    plant_1.name = "Rose"
    plant_1.height = 25
    plant_1.age = 30

    plant_2.name = "Tulip"
    plant_2.height = 20
    plant_2.age = 15

    plant_3.name = "Sunflower"
    plant_3.height = 75
    plant_3.age = 50

    print("=== Garden Plant Registry ===")
    print(f"{plant_1.name}: {plant_1.height}cm, {plant_1.age} days old")
    print(f"{plant_2.name}: {plant_2.height}cm, {plant_2.age} days old")
    print(f"{plant_3.name}: {plant_3.height}cm, {plant_3.age} days old")

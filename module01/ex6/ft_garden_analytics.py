class Garden:
    def __init__(self, owner: str):
        self.__owner = owner
        plants = []


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.__initial_height = height
        self.__total_growth = height - self.__initial_height


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color: str, bloom: bool) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloom = bloom


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, bloom, p_pts: int) -> None:
        super().__init__(name, height, age, color, bloom)
        self.prize_pts = p_pts


class GardenManager:
    @staticmethod
    def create_garden(owner: str) -> Garden:
        new_garden = Garden(owner)
        print(f"{owner}'s Garden was created successfully")
        return new_garden

    @staticmethod
    def display_info(garden: Garden):
        pass

    @staticmethod
    def add_to_garden(garden: Garden, plant_info: tuple) -> None:
        name = plant_info[0]
        height = plant_info[1]
        age = plant_info[2]
        plant = Plant(name, height, age)
        garden.plants.append(plant)
        print(f"Added {plant.name} to {garden.owner}'s Garden")
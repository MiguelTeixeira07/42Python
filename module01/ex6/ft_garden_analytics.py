class Garden:
    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        self.__initial_height = height
        self.__total_growth = height - self.__initial_height

    def get_info(self):
        print(f"- {self.name}:\n\t-> Height: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color: str, bloom: bool) -> None:
        super().__init__(name, height)
        self.color = color
        self.bloom = bloom

    def get_info(self):
        super().get_info()
        print(f"\t-> Color: {self.color} {'(blooming)'*(self.bloom)}")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, bloom, p_pts: int) -> None:
        super().__init__(name, height, color, bloom)
        self.prize_pts = p_pts

    def get_info(self):
        super().get_info()
        print(f"\t-> Prize points: {self.prize_pts}")


class GardenManager:
    garden_owners = []
    @classmethod
    def create_garden_network(cls, owners: list) -> list:
        new_gardens = []
        for owner in owners:
            new_gardens.append(Garden(owner))
            print(f"{owner}'s Garden was created successfully")
            cls.garden_owners.append(owner)
        return new_gardens

    @staticmethod
    def garden_report(garden: Garden) -> None:
        print(f"=== {garden.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in garden.plants:
            plant.get_info()
            print()

    @staticmethod
    def add_to_garden(garden: Garden, plant_info: list) -> None:
        match plant_info[0]:
            case "plant":
                plant = Plant(*plant_info[1:])
            case "flowering_plant":
                plant = FloweringPlant(*plant_info[1:])
            case "prize_flower":
                plant = PrizeFlower(*plant_info[1:])

        garden.plants.append(plant)
        print(f"Added {plant.name} to {garden.owner}'s Garden")


if __name__ == '__main__':
    print("=== Create a Garden ===")
    name = input("Enter your name: ")
    my_garden = GardenManager.create_garden_network(name)
    print()

    print(f"=== Add Plants to {name}'s Garden")
    while(True):
        type = input("Enter your plant's type (blank to stop): ")
        if type == '':
            break
        name = input("Enter your plant's name: ")
        height = int(input("Enter your plant's height: "))
        plant_info = [type, name, height]
        if type != "plant":
            color = input("Enter your plant's color: ")
            if input("Is your flower blooming? (y/n): ") == "y":
                bloom = True
            else:
                bloom = False
            plant_info.extend([color, bloom])
            if type == "prize_flower":
                prize_points = int(input("Enter your plant's prize points: "))
                plant_info.append(prize_points)
        GardenManager.add_to_garden(my_garden, plant_info)
        print()

    GardenManager.garden_report(my_garden)

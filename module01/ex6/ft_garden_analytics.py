class Garden:
    def __init__(self, owner: str):
        self.owner = owner
        self.plants: list[Plant | FloweringPlant | PrizeFlower] = []


class Plant:
    def __init__(self, type: str, name: str, height: int) -> None:
        self.type = type
        self.name = name
        self.height = height
        self.initial_height = height

    def get_info(self):
        print(f"- {self.name}\n\t-> Height: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, type, name, height, color: str, bloom: bool) -> None:
        super().__init__(type, name, height)
        self.color = color
        self.bloom = bloom

    def get_info(self):
        super().get_info()
        print(f"\t-> Color: {self.color} {'(blooming)'*(self.bloom)}")


class PrizeFlower(FloweringPlant):
    def __init__(self, type, name, height, color, bloom, p_pts: int) -> None:
        super().__init__(type, name, height, color, bloom)
        self.prize_pts = p_pts

    def get_info(self):
        super().get_info()
        print(f"\t-> Prize points: {self.prize_pts}")


class GardenManager:
    gardens = []

    class GardenStats:
        def __init__(self, garden: Garden):
            self.get_average_height(garden)
            self.get_growth(garden)
            self.get_plant_names(garden)
            self.get_total_prize_points(garden)
            self.plant_ammount(garden)

        def get_average_height(self, garden: Garden) -> None:
            sum = 0
            length = 0
            for plant in garden.plants:
                sum += plant.height
                length += 1
            self.av_height = sum / length

        def get_growth(self, garden: Garden):
            self.growth = []
            for plant in garden.plants:
                growth = plant.height - plant.initial_height
                self.growth.append(growth)

        def plant_ammount(self, garden: Garden):
            count = 0
            for _ in garden.plants:
                count += 1
            self.plants_added = count

        def get_plant_names(self, garden: Garden):
            self.name_type = []
            for plant in garden.plants:
                self.name_type.append({"name": plant.name, "type": plant.type})

        def get_total_prize_points(self, garden: Garden) -> None:
            self.total_prize_points = 0
            for plant in garden.plants:
                if plant.type == "Prize Flower":
                    self.total_prize_points += plant.prize_pts

    @classmethod
    def create_garden_network(cls, owner) -> Garden:
        new_garden = Garden(owner)
        print(f"{owner}'s Garden was created successfully")
        cls.gardens.append(new_garden)
        return new_garden

    @classmethod
    def garden_report(cls, garden: Garden) -> None:
        i = 0
        print(f"=== {garden.owner}'s Garden Report ===")
        stats = cls.GardenStats(garden)
        print("Plants in garden:")
        for plant in garden.plants:
            print(f"({stats.name_type[i]["type"]}): ", end='')
            plant.get_info()
            print(f"{stats.name_type[i]["name"]} grew {stats.growth[i]}cm!")
            i += 1
            print()
        print()
        print("== Garden Stats ==")
        print(f"Your garden currently has {stats.plants_added} plants")
        print(f"Average garden plant height: {stats.av_height}")
        print(f"Total prize points: {stats.total_prize_points}")
        i = 0
        for _ in cls.gardens:
            i += 1
        print(f"You are currently managing {i} gardens")

    @staticmethod
    def add_to_garden(garden: Garden, plant_info: list) -> None:
        match plant_info[0]:
            case "Plant":
                plant = Plant(*plant_info)
            case "Flowering Plant":
                plant = FloweringPlant(*plant_info)
            case "Prize Flower":
                plant = PrizeFlower(*plant_info)
            case _:
                print("Plant type is invalid")
                return

        garden.plants.append(plant)
        print(f"Added {plant.name} to {garden.owner}'s Garden")


if __name__ == '__main__':
    print("=== Create a Garden ===")
    name = input("Enter your name: ")
    my_garden = GardenManager.create_garden_network(name)
    print()

    print(f"=== Add Plants to {name}'s Garden")
    while True:
        type = input("Enter your plant's type (blank to stop): ")
        if type == '':
            break
        name = input("Enter your plant's name: ")
        height = int(input("Enter your plant's height: "))
        plant_info = [type, name, height]
        if type != "Plant":
            color = input("Enter your plant's color: ")
            if input("Is your flower blooming? (y/n): ") == "y":
                bloom = True
            else:
                bloom = False
            plant_info.extend([color, bloom])
            if type == "Prize Flower":
                prize_points = int(input("Enter your plant's prize points: "))
                plant_info.append(prize_points)
        GardenManager.add_to_garden(my_garden, plant_info)
        print()

    GardenManager.garden_report(my_garden)

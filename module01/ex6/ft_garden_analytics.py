class Garden:
    """Represents a garden owned by a single person."""

    def __init__(self, owner: str):
        """Create a new garden for the given owner."""
        self.owner = owner
        self.plants: list[Plant | FloweringPlant | PrizeFlower] = []


class Plant:
    """Basic plant with a name, type, and height."""

    def __init__(self, type: str, name: str, height: int) -> None:
        """Initialize a plant with type, name, and height."""
        self.type = type
        self.name = name
        self.height = height
        self.initial_height = height

    def get_info(self):
        """Print basic information about the plant."""
        print(f"- {self.name}\n\t-> Height: {self.height}cm")


class FloweringPlant(Plant):
    """A plant that has flowers and can bloom."""

    def __init__(self, type, name, height, color: str, bloom: bool) -> None:
        """Initialize a flowering plant with color and bloom status."""
        super().__init__(type, name, height)
        self.color = color
        self.bloom = bloom

    def get_info(self):
        """Print plant info including flower color and bloom status."""
        super().get_info()
        print(f"\t-> Color: {self.color} {'(blooming)'*(self.bloom)}")


class PrizeFlower(FloweringPlant):
    """A special flowering plant that awards prize points."""

    def __init__(self, type, name, height, color, bloom, p_pts: int) -> None:
        """Initialize a prize flower with prize points."""
        super().__init__(type, name, height, color, bloom)
        self.prize_pts = p_pts

    def get_info(self):
        """Print plant info including prize points."""
        super().get_info()
        print(f"\t-> Prize points: {self.prize_pts}")


class GardenManager:
    """Manages multiple gardens and generates reports."""

    gardens = []

    class GardenStats:
        """Calculates and stores statistics for a garden."""

        def __init__(self, garden: Garden):
            """Generate all statistics for the given garden."""
            self.get_average_height(garden)
            self.get_growth(garden)
            self.get_plant_names(garden)
            self.get_total_prize_points(garden)
            self.plant_ammount(garden)

        def get_average_height(self, garden: Garden) -> None:
            """Calculate the average height of plants in the garden."""
            sum = 0
            length = 0
            for plant in garden.plants:
                sum += plant.height
                length += 1
            self.av_height = sum / length

        def get_growth(self, garden: Garden):
            """Calculate how much each plant has grown."""
            self.growth = []
            for plant in garden.plants:
                growth = plant.height - plant.initial_height
                self.growth.append(growth)

        def plant_ammount(self, garden: Garden):
            """Count how many plants are in the garden."""
            count = 0
            for _ in garden.plants:
                count += 1
            self.plants_added = count

        def get_plant_names(self, garden: Garden):
            """Store plant names and types."""
            self.name_type = []
            for plant in garden.plants:
                self.name_type.append({"name": plant.name, "type": plant.type})

        def get_total_prize_points(self, garden: Garden) -> None:
            """Calculate total prize points in the garden."""
            self.total_prize_points = 0
            for plant in garden.plants:
                if plant.type == "Prize Flower":
                    self.total_prize_points += plant.prize_pts

    @classmethod
    def create_garden_network(cls, owner) -> Garden:
        """Create a new garden and add it to the manager."""
        new_garden = Garden(owner)
        print(f"{owner}'s Garden was created successfully")
        cls.gardens.append(new_garden)
        return new_garden

    @classmethod
    def garden_report(cls, garden: Garden) -> None:
        """Print a full report of the garden and its statistics."""
        i = 0
        print(f"=== {garden.owner}'s Garden Report ===")
        stats = cls.GardenStats(garden)
        print("Plants in garden:")
        for plant in garden.plants:
            print(f"({stats.name_type[i]['type']}): ", end='')
            plant.get_info()
            print(f"{stats.name_type[i]['name']} grew {stats.growth[i]}cm!")
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
        """Create a plant from input data and add it to the garden."""
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

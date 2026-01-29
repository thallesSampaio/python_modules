class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        self.initial_height = height

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def info(self) -> str:
        return f"{self.name}: {self.height}cm"

    @staticmethod
    def get_type() -> str:
        return "regular"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.blooming = True

    def info(self) -> str:
        return f"{super().info()}, {self.color} flowers (blooming)"

    @staticmethod
    def get_type() -> str:
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(
            self,
            name: str,
            height: int,
            color: str,
            prize_points: int
            ) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def info(self) -> str:
        return (f"{super().info()}, Prize points: {self.prize_points}")

    @staticmethod
    def get_type() -> str:
        return "prize"


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def add_plant_silence(self, plant: Plant) -> None:
        self.plants.append(plant)

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()


class GardenManager:
    total_gardens = 0

    class GardenStats:
        @staticmethod
        def total_growth(garden: Garden) -> int:
            total = 0
            for plant in garden.plants:
                total += plant.height - plant.initial_height
            return total

        @staticmethod
        def plant_types_count(garden: Garden) -> tuple[int, int, int]:
            regular = 0
            flowering = 0
            prize = 0
            for plant in garden.plants:
                if plant.get_type() == "prize":
                    prize += 1
                elif plant.get_type() == "flowering":
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        @staticmethod
        def garden_score(garden: Garden) -> int:
            score = 0
            for plant in garden.plants:
                score += plant.height
                if plant.get_type() == "prize":
                    score += plant.prize_points * 4
            return score

    def __init__(self) -> None:
        self.gardens = []

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)
        GardenManager.total_gardens += 1

    def report(self, garden: Garden) -> None:
        print(f"=== {garden.owner}'s Garden Report ===")
        print("Plants in garden:")
        total_plants = 0
        for plant in garden.plants:
            print(f"- {plant.info()}")
            total_plants += 1
        total_growth = self.GardenStats.total_growth(garden)
        print(f"\nPlants added: {total_plants}, "
              f"Total growth: {total_growth}cm")
        regular, flowering, prize = self.GardenStats.plant_types_count(garden)
        print(f"Plant types: {regular} regular,"
              f" {flowering} flowering,"
              f" {prize} prize flowers\n")

    @classmethod
    def create_garden_network(cls) -> str:
        return f"Total gardens managed: {cls.total_gardens}"

    @staticmethod
    def validate_heights(garden: Garden) -> bool:
        for plant in garden.plants:
            if plant.height < 0:
                return False
        return True


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    manager = GardenManager()
    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    bob_garden.add_plant_silence(Plant("BobPlant", 92))
    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    print()
    alice_garden.grow_all()
    print()
    manager.report(alice_garden)
    print(f"Height validation test: {manager.validate_heights(alice_garden)}")

    alice_score = manager.GardenStats.garden_score(alice_garden)
    bob_score = manager.GardenStats.garden_score(bob_garden)

    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(GardenManager.create_garden_network())

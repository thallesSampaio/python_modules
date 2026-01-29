class Plant:
    def __init__(self, name: str, start_height: int, start_age: int) -> None:
        self.name = name
        self.start_height = start_height
        self.start_age = start_age

    def print_plant(self) -> None:
        print(
            f"Created: {self.name} "
            f"({self.start_height}cm, {self.start_age} days)"
            )


class PlantFactory:
    def create_plants(data: dict) -> list:
        garden = []
        for name, value in data.items():
            height, age = value
            garden.append(Plant(name, height, age))
        return garden


if __name__ == "__main__":
    plants_data = {
        "Rose": [25, 30],
        "Oak": [200, 365],
        "Cactus": [5, 90],
        "Sunflower": [80, 45],
        "Fern": [15, 120],
    }
    garden = PlantFactory.create_plants(plants_data)
    print("=== Plant Factory Output ===")
    total_plants = 0
    for plant in garden:
        plant.print_plant()
        total_plants += 1
    print(f"\nTotal plants created: {total_plants} ")

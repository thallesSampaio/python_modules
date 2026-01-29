class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self, type) -> str:
        return f"{self.name} ({type}): {self.height}cm, {self.age} days, "


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            trunk_diameter: int
            ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        print(
            f"{self.name} provides {int(3.14 * ((self.height / 100) ** 2))}"
            " square meters of shade")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: int,
            age: int,
            harvest_season: str,
            nutritional_value: str
            ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    f1 = Flower("Rose", 25, 30, "red")
    f2 = Flower("Tulip", 30, 25, "orange")
    t1 = Tree("Oak", 500, 1825, 50)
    t2 = Tree("Basswood", 300, 2000, 10)
    v1 = Vegetable("Tomato", 80, 90, "summer", "High in Vitamin C")
    v2 = Vegetable("Potato", 40, 45, "winter", "High in Vitamin A")

    print(f"{f1.get_info("Flower")}{f1.color} color")
    f1.bloom()
    print(f"{t1.get_info("Tree")}{t1.trunk_diameter}cm diameter")
    t1.produce_shade()
    print()
    print(f"{v1.get_info("Vegetable")}{v1.harvest_season} harvest")
    print(f"{v1.name} is rich in {v1.nutritional_value}")

class Plant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.age_days += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    garden = [rose]
    start_height = rose.height
    print("=== Day 1 ===")
    for plant in garden:
        plant.get_info()

    for _ in range(6):
        for plant in garden:
            plant.grow()
            plant.age()

    print("=== Day 7 ===")
    for plant in garden:
        plant.get_info()
    print(f"Growth this week: +{rose.height - start_height}cm")

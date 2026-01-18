class Plant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    arr = [plant1, plant2, plant3]
    print("=== Garden Plant Registry ===")
    i = 0
    while i < 3:
        print(f"{arr[i].name}: {arr[i].height}cm, {arr[i].age_days} days old")
        i += 1

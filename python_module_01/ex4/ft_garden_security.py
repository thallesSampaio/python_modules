class SecurePlant:
    def __init__(self, name: str) -> None:
        self.name = name
        self._height = 0
        self._age = 0
        print("Plant created:", self.name)

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> int:
        return self._height

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days [OK]")

    def set_height(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-5)
    print(
            f"\nCurrent plant: {plant.name} "
            f"({plant.get_height()}cm, {plant.get_age()} days)"
        )

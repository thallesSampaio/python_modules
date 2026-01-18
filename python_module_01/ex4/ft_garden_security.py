class SecurePlant:
    def __init__(self, name) -> None:
        self.name = name
        self.__height = 0
        self.__age = 0
        print("Plant created:", self.name)

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def set_age(self, value: int):
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = value
            print(f"Age updated: {value} days [OK]")

    def set_height(self, value: int):
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = value
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

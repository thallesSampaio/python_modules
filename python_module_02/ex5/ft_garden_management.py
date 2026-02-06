class GardenError(Exception):
    """Base class for all garden errors."""
    pass


class PlantError(GardenError):
    """Errors related to plant name or existence."""
    pass


class WaterError(GardenError):
    """Errors related to watering levels or system."""
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[str] = []

    def add_plant(self, name: str) -> None:
        """Adds a plant to the list or raises PlantError if invalid."""
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(name)
        print(f"Added {name} successfully")

    def water_all_plants(self) -> None:
        """Waters all plants with mandatory cleanup using finally."""
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, name: str, water: int, sun: int) -> None:
        """Validates plant health parameters and raises errors if invalid."""
        if water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")
        if sun < 2:
            raise ValueError(f"Sunlight hours {sun} is too low (min 2)")
        print(f"{name}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    """Demonstrates integration of all error handling techniques."""
    print("=== Garden Management System ===")
    manager = GardenManager()

    print("\nAdding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant("")
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    manager.water_all_plants()

    print("\nChecking plant health...")
    try:
        manager.check_health("tomato", 5, 8)
    except ValueError as e:
        print(f"Error checking tomato: {e}")

    try:
        manager.check_health("lettuce", 15, 8)
    except ValueError as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()

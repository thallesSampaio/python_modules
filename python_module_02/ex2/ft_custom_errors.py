class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(hydrated: bool) -> None:
    if hydrated is False:
        raise PlantError("The tomato plant is wilting!")


def check_water(tank_empty: bool) -> None:
    if tank_empty is True:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    try:
        print("\nTesting PlantError...")
        check_plant(False)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    try:
        print("\nTesting WaterError...")
        check_water(True)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nTesting catching all garden errors...")
    try:
        check_plant(False)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        check_water(True)
    except GardenError as e:
        print(f"Caught a garden error: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_custom_errors()
    print("\nAll custom error types work correctly!")

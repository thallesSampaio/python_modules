class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    try:
        print("Testing PlantError...")
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    try:
        print("Testing WaterError...")
        check_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")
    for test in (check_plant, check_water):
        try:
            test()
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    print()
    print("All custom error types work correctly!")

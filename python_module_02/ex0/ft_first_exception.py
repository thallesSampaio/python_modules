def check_temperature(temp_str: str) -> int | None:
    """
    Tries to convert input and validates temperature range.
    Returns the temperature if valid, otherwise returns None.
    """
    try:
        temp_nbr: int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None
    else:
        if temp_nbr < 0:
            print(f"Error: {temp_nbr}°C is too cold for plants (min 0°C)\n")
            return None
        elif temp_nbr > 40:
            print(f"Error: {temp_nbr}°C is too hot for plants (max 40°C)\n")
            return None
        else:
            print(f"Temperature {temp_nbr}°C is perfect for plants!\n")
            return temp_nbr


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    tests = ["25", "abc", "100", "-50"]
    for test in tests:
        print(f"Testing temperature: {test}")
        check_temperature(test)
    print("All tests completed - program didn't crash!")

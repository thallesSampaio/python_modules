def check_temperature(temp_str: str) -> None:
    try:
        temp_nbr: int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
    else:
        if temp_nbr < 0:
            print(f"Error: {temp_nbr}°C is too cold for plants (min 0°C)\n")
        elif temp_nbr > 40:
            print(f"Error: {temp_nbr}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Temperature {temp_nbr}°C is perfect for plants!\n")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    check_temperature(input("Testing temperature: "))
    check_temperature(input("Testing temperature: "))
    check_temperature(input("Testing temperature: "))
    check_temperature(input("Testing temperature: "))
    print("All tests completed - program didn't crash!")

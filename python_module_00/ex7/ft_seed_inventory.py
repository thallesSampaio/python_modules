def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if unit == "packets":
        unit_str = str(quantity) + " packets available"
    elif unit == "grams":
        unit_str = str(quantity) + " grams total"
    elif unit == "area":
        unit_str = "covers " + str(quantity) + " square meters"
    else:
        print("Unknown unit type")
        return
    print(seed_type + " seeds: " + unit_str)

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    try:
        if artifacts == []:
            raise ValueError("Artifact list cannot be empty.")
        if not isinstance(artifacts, list):
            raise TypeError("Input must be a list of dictionaries.")
        for x in artifacts:
            if not isinstance(x, dict):
                raise TypeError("Each artifact must be a dictionary.")
        return sorted(artifacts, key=lambda x: x["power"], reverse=True)
    except Exception as e:
        print(f"Error occurred: {e.__class__.__name__} - {e}")
        return []


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    try:
        if mages == []:
            raise ValueError("Mage list cannot be empty.")
        if not isinstance(mages, list):
            raise TypeError("Input must be a list of dictionaries.")
        for x in mages:
            if not isinstance(x, dict):
                raise TypeError("Each mage must be a dictionary.")
        return list(filter(lambda x: x["power"] >= min_power, mages))
    except Exception as e:
        print(f"Error occurred: {e.__class__.__name__} - {e}")
        return []


def spell_transformer(spells: list[str]) -> list[str]:
    try:
        if spells == []:
            raise ValueError("Spell list cannot be empty.")
        if not isinstance(spells, list):
            raise TypeError("Input must be a list of strings.")
        for x in spells:
            if not isinstance(x, str):
                raise TypeError("Each spell must be a string.")
        return list(map(lambda x: "* " + x + " *", spells))
    except Exception as e:
        print(f"Error occurred: {e.__class__.__name__} - {e}")
        return []


def mage_stats(mages: list[dict]) -> dict:
    try:
        if mages == []:
            raise ValueError("Mage list cannot be empty.")
        if not isinstance(mages, list):
            raise TypeError("Input must be a list of dictionaries.")
        for x in mages:
            if not isinstance(x, dict):
                raise TypeError("Each mage must be a dictionary.")
        return {
            "max_power": max(mages, key=lambda x: x["power"]),
            "min_power": min(mages, key=lambda x: x["power"]),
            "avg_power": sum(map(lambda x: x["power"], mages)) / len(mages)
        }
    except Exception as e:
        print(f"Error occurred: {e.__class__.__name__} - {e}")
        return {}


if __name__ == "__main__":
    print("\nTesting artifact sorter...")
    artifacts = [{'name': 'Fire Staff', 'power': 92, 'type': 'focus'},
                 {'name': 'Crystal Orb', 'power': 85, 'type': 'accessory'}]
    res = artifact_sorter(artifacts)
    if res:
        print(f"{res[0]['name']} ({res[0]['power']} power) comes before "
              f"{res[1]['name']} ({res[1]['power']} power)")

    print("\nTesting power filter...")
    mages = [{'name': 'Rowan', 'power': 59, 'element': 'ice'},
             {'name': 'Morgan', 'power': 91, 'element': 'lightning'},
             {'name': 'Luna', 'power': 98, 'element': 'earth'},
             {'name': 'Sage', 'power': 96, 'element': 'light'},
             {'name': 'Ash', 'power': 71, 'element': 'wind'}]
    filtered = power_filter(mages, 90)
    if filtered:
        print("Power greater than or equal to 90:")
        for mage in filtered:
            print(f"{mage['name']} ({mage['power']} power)")

    print("\nTesting spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    transformed = spell_transformer(spells)
    if transformed:
        print("Transformed spells:")
        for spell in transformed:
            print(spell, end=" ")

    print("\n\nTesting mage stats...")
    stats = mage_stats(mages)
    if stats:
        print(f"Max power: {stats['max_power']['name']}"
              f"({stats['max_power']['power']} power)")
        print(f"Min power: {stats['min_power']['name']}"
              f"({stats['min_power']['power']} power)")
        print(f"Average power: {round(stats['avg_power'], 2)}")

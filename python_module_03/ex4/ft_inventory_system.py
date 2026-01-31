import sys


def parse_inventory() -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        if ":" in arg:
            name, qty = arg.split(":")
            inventory[name] = int(qty)
    return inventory


def analyze_inventory(inv: dict[str, int]) -> None:
    if not inv:
        print("Inventory is empty!")
        return

    total_units: int = sum(inv.values())
    unique_types: int = len(inv)
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_units}")
    print(f"Unique item types: {unique_types}")

    print("\n=== Current Inventory ===")
    sorted_items = sorted(inv.items(), key=lambda x: x[1], reverse=True)
    for name, qty in sorted_items:
        percentage: float = (qty / total_units) * 100
        unit_str: str = "unit" if qty == 1 else "units"
        print(f"{name}: {qty} {unit_str} ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")
    most_name: str = max(inv, key=inv.get)
    least_name: str = min(inv, key=inv.get)
    print(f"Most abundant: {most_name} ({inv[most_name]} units)")
    print(f"Least abundant: {least_name} ({inv[least_name]} units)")

    print("\n=== Item Categories ===")
    categories: dict[str, dict[str, int]] = {"Moderate": {}, "Scarce": {}}
    for name, qty in inv.items():
        if qty >= 5:
            categories["Moderate"][name] = qty
        else:
            categories["Scarce"][name] = qty
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")

    print("\n=== Management Suggestions ===")
    min_val: int = min(inv.values())
    restock: list[str] = [n for n, q in inv.items() if q == min_val]
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inv.keys())}")
    print(f"Dictionary values: {list(inv.values())}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inv}")


if __name__ == "__main__":
    current_inv: dict[str, int] = parse_inventory()
    analyze_inventory(current_inv)

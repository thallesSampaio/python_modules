import sys


def parse_inventory() -> dict[str, int]:
    inventory: dict[str, int] = {}
    if len(sys.argv) < 2:
        print("Usage: python ft_inventory_system.py item1:qty1 item2:qty2 ...")
        return
    for arg in sys.argv[1:]:
        if ":" in arg:
            name, qty = arg.split(":")
            try:
                inventory[name] = int(qty)
            except ValueError:
                print(f"Invalid quantity for item '{name}'")
                return {}
    return inventory


def ft_sum(dict: dict[str, int]) -> int:
    total: int = 0
    for value in dict.values():
        total += value
    return total


def sort_inventory(inv: dict[str, int]) -> list[tuple[str, int]]:
    items_list = [[k, v] for k, v in inv.items()]
    n = len(items_list)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if items_list[j+1][1] > items_list[j][1]:
                temp = items_list[j]
                items_list[j] = items_list[j+1]
                items_list[j+1] = temp
            j += 1
        i += 1
    return items_list


def current_inventory(items_list: list, total_units: int) -> None:
    print("\n=== Current Inventory ===")
    for name, qty in items_list:
        percentage: float = (qty / total_units) * 100
        unit_str: str = "unit" if qty == 1 else "units"
        print(f"{name}: {qty} {unit_str} ({percentage:.1f}%)")


def inventory_stats(items_list: list) -> None:
    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {items_list[0][0]} ({items_list[0][1]} units)")
    print(f"Least abundant: {items_list[3][0]} ({items_list[3][1]} unit)")


def item_cats(inv: dict[str, int]) -> None:
    moderate = dict()
    scarce = dict()
    for name, qty in inv.items():
        if qty >= 5:
            moderate.update({name: qty})
        else:
            scarce.update({name: qty})
    print("\n=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")


def analyze_inventory(inv: dict[str, int]) -> None:
    if not inv:
        print("Inventory is empty!")
        return

    total_units: int = ft_sum(inv)
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_units}")
    print(f"Unique item types: {len(inv)}")

    items_list = sort_inventory(inv)
    current_inventory(items_list, total_units)
    inventory_stats(items_list)
    item_cats(inv)

    print("\n=== Management Suggestions ===")
    restock = []
    for item_name in inv.keys():
        if inv[item_name] < 2:
            restock.append(item_name)
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    keys = [k for k in inv.keys()]
    values = [v for v in inv.values()]
    print(f"Dictionary keys: {keys}")
    print(f"Dictionary values: {values}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inv}")


if __name__ == "__main__":
    current_inv: dict[str, int] = parse_inventory()
    analyze_inventory(current_inv)

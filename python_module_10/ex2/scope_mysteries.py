from typing import Any


def mage_counter() -> callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    if initial_power.__class__ != int:
        raise TypeError("Initial power must be a integer.")
    total_power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total_power
        if amount.__class__ != int:
            raise TypeError("Amount value must be a integer.")
        total_power += amount
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    if enchantment_type.__class__ != str:
        raise TypeError("Enchantment type must be string.")

    def enchant(item_name: str):
        if item_name.__class__ != str:
            raise TypeError("Item name must be string.")
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, callable]:
    vault = {}

    def store(key: str, value: Any) -> None:
        if key.__class__ != str:
            raise KeyError("Memory keys must be strings.")
        vault[key] = value

    def recall(key: str) -> str:
        if key.__class__ != str:
            raise KeyError("Memory keys must be strings.")
        return vault.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":
    print("\nTesting mage counter...")
    res = mage_counter()
    print(f"Call 1: {res()}")
    print(f"Call 2: {res()}")
    print(f"Call 3: {res()}")

    print("\nTesting spell accumulator...")
    try:
        accumulator = spell_accumulator(13)
        print(f"Call 1: {accumulator(3)}")
        print(f"Call 2: {accumulator(4)}")
        print(f"Call 3: {accumulator(5)}")
    except Exception as e:
        print(f"Error: {e}")

    print("\nTesting enchantment factory...")
    try:
        flaming = enchantment_factory("Flaming")
        frozen = enchantment_factory("Frozen")
        print(flaming("Sword"))
        print(frozen("Shield"))
    except Exception as e:
        print(f"Error: {e}")

    print("\nTesting memory vault...")
    try:
        vault = memory_vault()
        vault["store"]("secret_password", "Secret Value")
        print(f"Recall: {vault['recall']('secret_password')}")
        print(f"Recall: {vault['recall']('unknown')}")
    except Exception as e:
        print(f"Error: {e}")

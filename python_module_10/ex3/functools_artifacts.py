from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:

    if not isinstance(spells, list):
        raise TypeError("TypeError Spells must be a list of integers.")
    if not spells:
        raise ValueError("ValueError Spells can't be empty.")
    for s in spells:
        if not isinstance(s, int):
            raise TypeError("TypeError Spells must be a list of integers.")

    if operation == "add":
        return reduce(add, spells)
    elif operation == "multiply":
        return reduce(mul, spells)
    elif operation == "max":
        return reduce(max, spells)
    elif operation == "min":
        return reduce(min, spells)
    else:
        raise ValueError(f"Unknow operation: '{operation}'.")


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    if not callable(base_enchantment):
        raise TypeError("TypeError: base_enchantment must be a callable.")

    return {
        "fire_enchant": partial(base_enchantment, power=50, element="fire"),
        "ice_enchant": partial(base_enchantment, power=50, element="ice"),
        "lightning_enchant": partial(base_enchantment, power=50,
                                     element="lightning")
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError(f"TypeError: '{n}' is not an integer.")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def dispatcher(arg: Any):
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(arg: int):
        return f"Casting damage spell: {arg} damage!"

    @dispatcher.register(str)
    def _(arg: str):
        return f"Casting enchantment: {arg}"

    @dispatcher.register(list)
    def _(arg: list):
        if not arg:
            raise ValueError("List cant be empty.")
        return f"Multi-casting: {', '.join(map(str, arg))}"

    return dispatcher


if __name__ == "__main__":
    try:
        print("\nTesting spell reducer...")
        sum = [20, 20, 20, 20, 20]
        product = [240, 100, 10]
        max_values = [1, 2, 39, 27, 40, 22]
        print(f"Sum: {spell_reducer(sum, 'add')}")
        print(f"Product: {spell_reducer(product, 'multiply')}")
        print(f"Max: {spell_reducer(max_values, 'max')}")
    except Exception as e:
        print(f"Error: {e}")

    try:
        print("\nTesting memoized fibonacci...")
        print(f"Fib(10): {memoized_fibonacci(10)}")
    except TypeError as e:
        print(f"Error: {e}")

    try:
        print("\nTesting partial enchanter...")

        def base_enchantment(target: str, power: int, element: str) -> str:
            return f"{target} attacked by {element} weapon with {power} power"
        res = partial_enchanter(base_enchantment)
        print(res["fire_enchant"]("dragon"))
        print(res['ice_enchant']('goblins'))
    except TypeError as e:
        print(f"Error: {e}")

    try:
        print("\nTesting spell dispatcher...")
        dispatch = spell_dispatcher()
        print(dispatch(100))
        print(dispatch("Invisibility"))
        print(dispatch([]))
    except ValueError as e:
        print(f"\nValueError: {e}")

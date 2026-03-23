from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }

    if operation not in ops:
        raise ValueError(f"Unknow operation: '{operation}'.")

    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, power=50, element="fire"),
        "ice_enchant": partial(base_enchantment, power=50, element="ice"),
        "lightning_enchant": partial(base_enchantment, power=50,
                                     element="lightning")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
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
        return f"Multi-casting: {', '.join(map(str, arg))}"

    return dispatcher


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    sum = [20, 20, 20, 20, 20]
    product = [240, 100, 10]
    max_values = [1, 2, 39, 27, 40, 22]
    print(f"Sum: {spell_reducer(sum, 'add')}")
    print(f"Product: {spell_reducer(product, 'multiply')}")
    print(f"Max: {spell_reducer(max_values, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")

    print("\nTesting partial enchanter...")

    def base_enchantment(target: str, power: int, element: str) -> str:
        return f"{target} attacked by {element} weapon with {power} power"
    res = partial_enchanter(base_enchantment)
    print(res["fire_enchant"]("dragon"))
    print(res['ice_enchant']('goblins'))

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(100))
    print(dispatch("Invisibility"))
    print(dispatch([1, 2, 3]))

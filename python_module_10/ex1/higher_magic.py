from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise ValueError("Both spells must be callable functions.")

    def combined(*args, **kwargs) -> tuple:
        return spell1(*args, **kwargs), spell2(*args, **kwargs)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise ValueError("Base spell must be callable function.")
    if multiplier.__class__ != int:
        raise TypeError(f"Multiplier must be an integer."
                        f" Received: '{multiplier}'"
                        f" type: ({multiplier.__class__})")

    def amplifier(*args, **kwargs) -> int | float:
        res = base_spell(*args, **kwargs)
        if res.__class__ != int:
            raise TypeError(f"Base spell returned {res.__class__.__name__}, "
                            "but a integer is required for amplification.")
        return res * multiplier
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition) or not callable(spell):
        raise ValueError("Both spells must be callable functions.")

    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args, **kwargs) -> list:
        results = []
        for spell in spells:
            if not callable(spell):
                raise ValueError(f"All spells must be callable. "
                                 f"Found {spell.__class__}: '{spell}'")
            res = spell(*args, **kwargs)
            results.append(res)
        return results
    return sequence


def combiner_demo() -> None:
    def fireball(target: str) -> str: return f"Fireball hits {target}"
    def heal(target: str) -> str: return f"Heals {target}"
    print("\nTesting spell combiner...")
    try:
        combined = spell_combiner(fireball, heal)
        res = combined("Dragon")
        print(f"Combined spell result: {res[0]}, {res[1]}")
    except Exception as e:
        print(f"Error: {e}")


def amplifier_demo() -> None:
    print("\nTesting power amplifier...")
    def spell(value: int) -> int: return value
    try:
        amplifier = power_amplifier(spell, 3)
        value: int = 10
        print(f"Original: {value}, Amplified: {amplifier(value)}")
    except Exception as e:
        print(f"Error: {e}")


def caster_demo() -> None:
    print("\nTesting conditional caster...")
    def spell(spell: str) -> str: return spell
    try:
        caster = conditional_caster(lambda x: True, spell)
        print(f"Casted: {caster("Lightning Bolt")}")
    except Exception as e:
        print(f"Error: {e}")


def sequence_demo() -> None:
    print("\nTesting spell sequence...")
    def ice_arrow(value: int) -> str: return f"Ice arrow power: {value}"
    def fireball(value: int) -> str: return f"Fireball power: {value}"
    def bolt(value: int) -> str: return f"Lightning bolt power: {value}"
    try:
        sequence = spell_sequence([ice_arrow, fireball, bolt])
        res = sequence(15)
        for s in res:
            print(s)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    combiner_demo()
    amplifier_demo()
    caster_demo()
    sequence_demo()

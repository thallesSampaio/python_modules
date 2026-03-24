import functools
import time


def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> any:
        start = time.time()
        print(f"Casting {func.__name__}...")
        res = func(*args, **kwargs)
        elapsed = round((time.time() - start), 3)
        print(f"Spell completed in {elapsed} seconds")
        return res
    return wrapper


def power_validator(min_power: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get('power')
            if power is None:
                power = args[2] if len(args) > 2 else args[1]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def retry(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            i = 1
            while i <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f'Spell failed, retrying... (attempt {i}/'
                          f'{max_attempts})')
                    i += 1
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return retry


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not len(name) >= 3:
            return False

        for letter in name:
            if (letter.isalpha() is False and letter != ' '):
                return False

        return True

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


if __name__ == "__main__":
    print("\nTesting spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)
        return "Fireball cast!"
    print(f"Result: {fireball()}")

    print("\nTesting mage guild...")

    mage = MageGuild()
    print(MageGuild.validate_mage_name(" Valid "))
    print(MageGuild.validate_mage_name("#invalid"))
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Lightning", 8))
    print()

    @retry_spell(5)
    def retry(spell_name: str) -> str:
        if not isinstance(spell_name, str):
            raise TypeError("VALUE MUST BE AN STRING")
        return f"Casting {spell_name}..."
    spells = ["fireball", "lightning bolt"]
    for s in spells:
        print(retry(s))

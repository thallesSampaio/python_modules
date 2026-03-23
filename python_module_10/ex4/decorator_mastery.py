import functools
import time

def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> None:
        start = time.time()
        print(f"Casting {func.__name__}")
        res = func(*args, **kwargs)
        latest = round((time.time() - start), 3)
        print(f"Spell completed in {latest} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> callable:
    ...


def retry_spell(max_attempts: int) -> callable:
    ...


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        ...


def cast_spell(self, spell_name: str, power: int) -> str:
    ...


if __name__ == "__main__":
    fdss = "fds"
    @spell_timer
    def test(fds):
        return f"fds{fds}"
    res = test(fdss)
    print(res)

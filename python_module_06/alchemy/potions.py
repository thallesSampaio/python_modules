from .elements import create_fire, create_water, create_earth, create_air


def healing_potion() -> str:
    fr = create_fire()
    wr = create_water()
    return f"Healing potion brewed with {fr} and {wr}"


def strength_potion() -> str:
    er = create_earth()
    fr = create_fire()
    return f"Strength potion brewed with {er} and {fr}"


def invisibility_potion() -> str:
    ar = create_air()
    wr = create_water()
    return f"Invisibility potion brewed with {ar} and {wr}"


def wisdom_potion() -> str:
    fr = create_fire()
    wr = create_water()
    er = create_earth()
    ar = create_air()
    return f"Wisdom potion brewed with all elements: {fr}, {wr}, {er} and {ar}"

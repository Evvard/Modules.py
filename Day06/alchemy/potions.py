from .elements import create_fire, create_water, create_earth
from .elements import create_air


def healing_potion() -> str:
    message = "Healing potion brewed with"
    return f"{message} {create_fire()} and {create_water()}"


def strength_potion() -> str:
    message = "Strength potion brewed with"
    return f"{message} {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    message = "Invisibility potion brewed with"
    return f"{message} {create_air()} and {create_water()}"

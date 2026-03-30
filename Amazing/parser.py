from typing import Any
from random import randint


def parse_value(value: Any) -> int | str | float:
    value = value.strip()
    if value.isdigit():
        return int(value)
    try:
        return float(value)
    except ValueError:
        return value


def pars_file() -> dict:
    try:
        data = dict({})
        with open("config.txt", 'r') as file:
            for line in file:
                try:
                    line = line.strip()
                    if not "=" in line:
                        raise ValueError
                    key, value = line.split("=", 1)
                    data[key] = parse_value(value)
                except ValueError:
                    pass
    except FileNotFoundError or PermissionError:
        print("Missing file")
    return {data}


def data_parser(data: dict) -> dict:
    good_data = dict({})
    for obj in data:

        if not "WIDTH" in good_data.key():
            if obj.key() == "WIDTH":
                try:
                    width = obj.get("WIDTH")

                    if width <= MINIMUM or width >= MAXIMUM:
                        raise Exception
                    good_data.update(obj)
                except KeyError or Exception:
                    value = randint(MINIMUM, MAXIMUM)
                    good_data.update({"WIDTH": value})


        if not "HEIGHT" in good_data.key():
            if obj.key() == "HEIGHT":
                try:
                    width = obj.get("HEIGHT")

                    if width <= MINIMUM or width >= MAXIMUM:
                        raise Exception
                    good_data.update(obj)
                except KeyError or Exception:
                    value = randint(MINIMUM, MAXIMUM)
                    good_data.update({"HEIGHT": value})

#Pareil pour Entry Exit et les autres parametres
#guette ensuite si il ya bien tout les argument dans good_data
#puis on retutrn

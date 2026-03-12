class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self) -> None:
        super().__init__("Caught PlantError: The tomato plant is wilting!")


class WaterError(GardenError):
    def __init__(self) -> None:
        super().__init__("Caught WaterError: Not enough water in the tank!")


def do_error(percentage_of_well_being: int, percentage_of_water: int,
             i: int) -> None:
    if i == 1:
        print("=== Custom Garden Errors Demo ===\n")

        print("Testing PlantError...")
    try:
        if int(percentage_of_well_being) < 75:
            raise PlantError()
    except ValueError:
        print("Caught ValueError: invalid literal for int()", "\n")
        return
    except PlantError as e:
        print(e)
    if i == 1:
        print
        print("Testing WaterError...")
    try:
        if int(percentage_of_water) < 75:
            raise WaterError()
    except ValueError:
        print("Caught ValueError: invalid literal for int()", "\n")
        return
    except WaterError as e:
        print(e, "\n")
    if i == 1:
        print("Testing catching all garden errors...")
    i += 1
    if (i <= 2):
        do_error(percentage_of_well_being, percentage_of_water, i)


if __name__ == "__main__":
    do_error(5, 5, 1)

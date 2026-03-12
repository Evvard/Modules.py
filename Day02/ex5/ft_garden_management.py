class GardenError(Exception):
    pass


class EmptyPlant(GardenError):
    def __init__(self) -> None:
        super().__init__("Error adding plant: Plant name cannot be empty")


class InvalidPlant(GardenError):
    def __init__(self) -> None:
        message = ("Error adding plant: Plant name cannot be")
        super().__init__(message, "other thing than a letter!")


class NoNumerciValue(GardenError):
    def __init__(self) -> None:
        super().__init__("water level and sunlight hours need to be numeric")


class WaterError(GardenError):
    def __init__(self, water: int) -> None:
        if water > 10:
            super().__init__(f"Water level {water} is too high (max 10)")
        else:
            super().__init__(f"Water level {water} is too low (min 1)")


class SunError(GardenError):
    def __init__(self, sun: int) -> None:
        if sun > 12:
            super().__init__(f"Sun level {sun} is too high (max 12)")
        else:
            super().__init__(f"Sun level {sun} is too low (min 2)")


class GardenManager:
    def __init__(self) -> None:
        self.plants = []
        self.water = []
        self.sun = []

    def add_plant(self, plants: list, ) -> None:
        print("Adding plants to garden...")
        try:
            for i in range(0, len(plants), 3):
                if not (plants[i] and plants[i + 1] and plants[i + 2]):
                    raise EmptyPlant()
                elif not plants[i].isalpha():
                    raise InvalidPlant()
                elif not (plants[i + 1].isdigit() and plants[i + 2].isdigit()):
                    raise NoNumerciValue
                else:
                    print(f"Added {plants[i]} successfully")
                    self.plants += [plants[i]]
                    self.water += [int(plants[i + 1])]
                    self.sun += [int(plants[i + 2])]
        except EmptyPlant as e:
            print(e)
        except InvalidPlant as e:
            print(e)
        except NoNumerciValue as e:
            print(e)

    def water_a_plant(self) -> None:
        print("\nWatering plants...\nOpening watering system")
        try:
            for i in range(len(self.plants)):
                if not self.plants:
                    raise GardenError("No plants to water!")
                print(f"Watering {self.water[i]} - success")
                self.water[i] += 1
        except Exception as e:
            print(f"Watering system encountered an error: {e}")
        finally:
            print("Closing watering system (cleanup)\n")

    def plant_health(self) -> None:
        print("Checking plant health...")

        for i in range(len(self.plants)):
            try:
                if self.water[i] > 10 or self.water[i] < 1:
                    raise WaterError(self.water[i])
                elif self.sun[i] > 12 or self.sun[i] < 2:
                    raise SunError({self.sun[i]})
                else:
                    print(f"{self.plants[i]}: healthy (water: ", end="")
                    print(f"{self.water[i]}, sun: {self.sun[i]})")
            except WaterError as e:
                print(f"Error checking {self.plants[i]}:", e)
                print()
            except SunError as e:
                print(f"Error checking {self.plants[i]}", e)
                print()


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    plants_atribuates = ["tomato", "5", "8",
                         "letuce", "15", "9",
                         "", "0", "test_erreur"]
    garden = GardenManager()
    garden.add_plant(plants_atribuates)
    garden.water_a_plant()
    garden.plant_health()
    print("Testing error recovery...")
    try:
        if int(plants_atribuates[7]) < 1:
            raise GardenError()
    except ValueError:
        print("The value is not int value bro")
    except GardenError:
        print("Caught GardenError: Not enough water in tank")
    finally:
        print("System recovered and continuing...\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()

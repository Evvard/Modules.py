class GardenManager:
    def __init__(self) -> None:
        self.plants = []
        self.water = []
        self.sun = []

    def add_plant(self, plants: list, ) -> None:
        print("Adding plants to garden...")
        try:
            for i in range(0, len(plants), 3):
                if not (i[0] and i[1] and i[2]):
                    raise ValueError
                elif not i[0].isapha():
                    raise Exception
                elif not (i[1] and i[2]).isdigit():
                    raise EOFError
                else:
                    print(f"Added {i[0]} successfully")
                    self.plants += i[0]
                    self.water += int(i[1])
                    self.sun += int(i[2])
        except ValueError:
            print("Error adding plant: Plant name cannot be empty!")
        except Exception:
            print("Error adding plant: Plant name cannot be", end="")
            print("other thing than a letter!")
        except EOFError:
            print("water level and sunlight hours need to be numeric")

    def water_a_plant(self):
        print("\nWatering plants...\nOpening watering system")
        for i in len(self.add_plant):
            print(f"Watering {i} - success")
            self.water[i] += 1
        print("Closing watering system (cleanup)")

    def plant_health(self):
        print("Checking plant health...")

        try:
            for i in len(self.plants):
                if self.water > 10:
                    raise ZeroDivisionError
                elif self.water < 1:
                    raise EOFError
                elif self.sun > 12:
                    raise ValueError
                elif self.sun < 2:
                    raise KeyError
                else:
                    print(f"{self.plants[i]}: healthy (water: ", end="")
                    print(f"{self.water[i]}, sun: {self.sun[i]})")
        except ZeroDivisionError:
            print(f"Error checking {self.plants[i]}: Water level", end=" ")
            print(f"{self.water[i]}, is too high (max 10)")
        except EOFError:
            print(f"Error checking {self.plants[i]}: Water level", end=" ")
            print(f"{self.water[i]}, is too low (min 1)")
        except ValueError:
            print(f"Error checking {self.plants[i]}: Sun level", end=" ")
            print(f"{self.sun[i]}, is too high (max 12)")
        except KeyError:
            print(f"Error checking {self.plants[i]}: Sun level", end=" ")
            print(f"{self.sun[i]}, is too low (min 2)")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    plants_atribuates = ["tomato", "5", "8",
                         "letuce", "15", "9",
                         "", "88", "test_erreur"]
    GardenManager.add_plant(plants_atribuates)
    GardenManager.water_a_plant()
    GardenManager.plant_health()
    print("Testing error recovery...")





    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
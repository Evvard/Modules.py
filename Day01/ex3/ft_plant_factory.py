class Plantes:

    plant_create = 0

    def __init__(self, name: str, size: int, days: int) -> None:
        self.name = name
        self.size = size
        self.days = days

    def printclass(self) -> None:
        print(f"Created: {self.name} ({self.size}cm, {self.days} days)")
        Plantes.plant_create += 1

    def return_plant_max() -> None:
        print(f"Total plants created: {Plantes.plant_create}")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    params = ["Rose", 25, 30,
              "Oak", 200, 365,
              "Cactus", 5, 9,
              "Sunflower", 80, 45,
              "Fern", 15, 120]
    i = 0
    y = 0
    i = len(params)
    while y < i:
        Plant = Plantes(params[y], params[y + 1], params[y + 2])
        Plant.printclass()
        y += 3
    Plantes.return_plant_max()

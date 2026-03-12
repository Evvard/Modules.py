class Plantes_Security:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.height = height
        self.age = age
        self.name = name

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print("Invalid operation attempted: age ", end="")
            print(f"{new_height} height [REJECTED]")
            print("Security: Negative age rejected")
            print()
        else:
            self._height = new_height
            print(f"Height updated: {self._height} days [OK]")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print("Invalid operation attempted: age", end="")
            print(f" {new_age} days [REJECTED]")
            print("Security: Negative age rejected")
            print()
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days [OK]")
            print()

    age = property(get_age, set_age)
    height = property(get_height, set_height)

    def __str__(self):
        return f"{self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = "Rose"
    print(f"Plant created: {plant}")
    Plant1 = Plantes_Security(plant, 25, 30)
    Plant1.age = -5
    print(f"Current plant: {Plant1}")

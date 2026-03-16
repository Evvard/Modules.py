class Plant:
    def __init__(self, name: str, age: int, days: int, grow: int) -> None:
        self.name = name
        self.age = age
        self.days = days
        self.grow = grow

    def function_class(self) -> None:
        print(f"{self.name}: {self.age}cm, {self.days} days old")

    def grow_print(self, nb_day: int) -> None:
        print(f"{self.name}: {self.age + self.grow}cm", end="")
        print(f" {self.days + nb_day} days old")


if __name__ == "__main__":
    growing = 6
    print("=== Day 1 ===")
    plant1 = Plant("Rose", 25, 30, growing)
    plant1.function_class()
    nb_day = growing
    print(f"=== Day {nb_day} ===")
    plant1.grow_print(nb_day)
    if growing >= 0:
        print(f"Growth this week: +{growing}cm")
    else:
        print(f"Growth this week: {growing}cm")

class Plant:
    def __init__(self, name: str, age: int, days: int) -> None:
        self.name = name
        self.age = age
        self.days = days

    def function_class(self) -> None:
        print(f"{self.name}: {self.age}cm, {self.days} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    plant1.function_class()
    plant2.function_class()
    plant3.function_class()

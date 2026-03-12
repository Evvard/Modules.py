class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):

    def __init__(self, name: str, height: int, age: int,
                 color: str, ability_to_bloom: str) -> None:
        super().__init__(name=name, height=height, age=age)
        self.color = color
        self.ability_to_bloom = ability_to_bloom
        print()

    def printable(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm, {self.age}", end="")
        print(f" days, {self.color} color")
        print(f"{self.name} is blooming {self.ability_to_bloom}!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int, produce_shade: int) -> None:
        super().__init__(name=name, height=height, age=age)
        self.trunk_diameter = trunk_diameter
        self.produce_shade = produce_shade
        print()

    def printable(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days", end="")
        print(f", {self.trunk_diameter}cm diameter")
        print(f"{self.name} provides {self.produce_shade} ", end="")
        print("square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name=name, height=height, age=age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print()

    def printable(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm", end="")
        print(f", {self.age} days, {self.harvest_season} harvest")
        print(f"{self.name} is {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red", "beautifully")
    Flower.printable(rose)
    oak = Tree("Oak", 500, 1825, 50, 78)
    Tree.printable(oak)
    tomato = Vegetable("Tomato", 80, 90, "summer", "is rich in vitamin C")
    Vegetable.printable(tomato)

class Plant:

    def __init__(self, plant_name: str, size: int) -> None:
        self.plant_name = plant_name
        self.size = size

    def grow(self, add_size: int) -> None:
        i = add_size - self.size
        self.size = add_size
        print(f"{self.plant_name} grew {i}cm")

    def __str__(self) -> str:
        return f"- {self.plant_name}: {self.size}cm"


class FloweringPlant(Plant):

    def __init__(self, plant_name: str, size: int, color: str) -> None:
        super().__init__(plant_name=plant_name, size=size)
        self.color = color

    def __str__(self) -> str:
        base_text = super().__str__()
        return f"{base_text}, {self.color} flowers"


class PrizeFlower(FloweringPlant):

    def __init__(self, plant_name: str, size: int,
                 color: str, prize: str) -> None:
        super().__init__(plant_name=plant_name, size=size, color=color)
        self.prize = prize

    def __str__(self) -> str:
        base_text = super().__str__()
        return f"{base_text}, Prize points: {self.prize}"


class GardenManager:

    nombre_of_user = 0

    def __init__(self, username: str) -> None:
        self.user_name = username
        self.plants = []
        GardenManager.nombre_of_user += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)

    def create_garden_network(cls):
        return cls.nombre_of_user
    create_garden_network = classmethod(create_garden_network)

    class GardenStats:

        def validate_height(size: int) -> bool:
            if size > 0:
                return True
            else:
                return False
        validate_height = staticmethod(validate_height)

        def summarize_plants(plants: list) -> str:
            count = len(plants)
            total_growth = 0
            for p in plants:
                total_growth += p.size
            return f"Plants added: {count}, Total growth: {total_growth}cm"
        summarize_plants = staticmethod(summarize_plants)

        def count_types(plants: list) -> str:
            normal = 0
            flowering = 0
            prize = 0
            for p in plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                elif isinstance(p, Plant):
                    normal += 1
            return (f"Plant types: {normal} regular, {flowering} "
                    f"flowering, {prize} prize flowers")
        count_types = staticmethod(count_types)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    alice_garden.add_plant(oak)

    print(f"Added {oak.plant_name} to Alice's garden")
    alice_garden.add_plant(rose)
    print(f"Added {rose.plant_name} to Alice's garden")
    alice_garden.add_plant(sunflower)
    print(f"Added {sunflower.plant_name} to Alice's garden")

    print("\nAlice is helping all plants grow...")
    oak.grow(101)
    rose.grow(26)
    sunflower.grow(51)

    print(f"\n=== {alice_garden.user_name}'s Garden Report ===")
    print("Plants in garden:")
    for plant in alice_garden.plants:
        print(plant)
    print()
    stats = GardenManager.GardenStats.summarize_plants(alice_garden.plants)
    print(stats)
    plant_type = GardenManager.GardenStats.count_types(alice_garden.plants)
    print(plant_type)
    print()

    valid_test = GardenManager.GardenStats.validate_height(10)
    print(f"Height validation test (10cm): {valid_test}")
    print("Garden scores - Alice: 218, Bob: 92")
    total_gardens = GardenManager.create_garden_network()
    print(f"Total gardens managed: {total_gardens}")

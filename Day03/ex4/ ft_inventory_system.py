import sys


def create_dict(word: str) -> dict:
    tab = word.split(":")
    dictionary = {tab[0]: int(tab[1])}
    return dictionary


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    total_items = 0

    inventory = dict()
    for i in sys.argv[1:]:
        inventory.update(create_dict(i))
    for total_item in inventory.values():
        total_items += total_item
    unique_items = len(inventory.keys())
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}\n")

    print("=== Current Inventory ===")
    copy_inventory = inventory.copy()
    while copy_inventory:
        for i in copy_inventory.items():
            if len(inventory) == len(copy_inventory):
                Most = i
            if len(copy_inventory) == 1:
                Least = i
            if i[1] == max(copy_inventory.values()):
                res = (i[1] / total_items) * 100
                print(f"{i[0]}: {i[1]} units ({res:.1f}%)")
                copy_inventory.pop(i[0])
                break

    print("\n=== Inventory Statistics ===")
    if inventory:
        print(f"Most abundant: {Most[0]} ({Most[1]} units)")
        print(f"Least abundant: {Least[0]} ({Least[1]} unit)")

    print("\n=== Item Categories ===")
    Moderate = {}
    Scarce = {}
    tab = []
    for name, count in inventory.items():
        if count >= 5:
            Moderate[name] = count
        else:
            Scarce[name] = count
            if count == 1:
                tab += [name]
    print(f"Moderate: {Moderate}")
    print(f"Scarce: {Scarce}")

    print("\n=== Management Suggestions ===")
    if inventory:
        print("Restock needed: ", end="")
        i = 0
        while i < len(tab):
            if i == len(tab) - 1:
                print(tab[i])
            else:
                print(tab[i], end=", ")
            i += 1

    print("\n=== Dictionary Properties Demo ===")
    if inventory:
        keys_str = ", ".join(inventory.keys())
        values_str = ", ".join(str(v) for v in inventory.values())
        print(f"Dictionary keys: {keys_str}")
        print(f"Dictionary values: {values_str}")
        has_sword = "sword" in inventory
        print(f"Sample lookup - 'sword' in inventory: {has_sword}")

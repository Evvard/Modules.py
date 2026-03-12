def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    i = seed_type.capitalize()
    quantity = int(quantity)
    if unit == "area" or unit == "AREA":
        print(i, "seeds: covers", quantity, "quare meters")
    elif unit == "packets" or unit == "PACKETS":
        print(i, "seeds:", quantity, "packets available")
    elif unit == "grams" or unit == "GRAMS":
        print(i, "seeds:", quantity, "grams total")
    else:
        print(i, "seeds:", quantity, "Unknown unit type")

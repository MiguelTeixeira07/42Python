def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type_cap = seed_type.capitalize()
    if unit == "packets":
        print(seed_type_cap, "seeds:", quantity, "packets available")
    elif unit == "grams":
        print(seed_type_cap, "seeds:", quantity, "grams total")
    elif unit == "area":
        print(seed_type_cap, "seeds: covers", quantity, "square meters")
    else:
        print("Unknown unit type")

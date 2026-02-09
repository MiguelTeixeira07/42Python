import sys


def parse_inventory(argv_items):
    inventory = dict()
    for arg in argv_items:
        try:
            name, qty = arg.split(":")
            qty = int(qty)
            inventory[name] = qty
        except Exception as e:
            print(f"Error parsing '{arg}': {e}")
    return inventory


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py item1:qty item2:qty ...")
        return

    inventory = parse_inventory(sys.argv[1:])

    total_items = 0
    for qty in inventory.values():
        total_items += qty

    unique_items = 0
    for _ in inventory.keys():
        unique_items += 1
    print()
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")
    print()
    print("=== Current Inventory ===")
    for item, qty in inventory.items():
        if total_items > 0:
            percent = (qty / total_items) * 100
        else:
            percent = 0
        print(f"{item}: {qty} unit{'s' if qty > 1 else ''} ({percent:.1f}%)")

    most_abundant_item = None
    least_abundant_item = None
    most_qty = -1
    least_qty = None
    for item, qty in inventory.items():
        if qty > most_qty:
            most_qty = qty
            most_abundant_item = item
        if least_qty is None or qty < least_qty:
            least_qty = qty
            least_abundant_item = item
    print()
    print("=== Inventory Statistics ===")
    print(f"Most abundant: {most_abundant_item} ({most_qty} units)")
    print(f"Least abundant: {least_abundant_item} ({least_qty} units)")

    moderate = dict()
    scarce = dict()
    for item, qty in inventory.items():
        if qty >= 5:
            moderate[item] = qty
        else:
            scarce[item] = qty
    print()
    print("=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    restock_needed = []
    for item, qty in scarce.items():
        if qty <= 1:
            restock_needed.append(item)
    print()
    print("=== Management Suggestions ===")
    print(f"Restock needed: {restock_needed}")
    print()
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    main()

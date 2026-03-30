import sys


def parse_inventory() -> tuple[dict, list]:
    inventory = {}
    order = []

    for arg in sys.argv[1:]:
        parts = arg.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item = parts[0]
        quantity_str = parts[1]

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            quantity = int(quantity_str)
        except Exception as error:
            print(f"Quantity error for '{item}': {error}")
            continue

        inventory[item] = quantity
        order.append(item)

    return inventory, order


def print_percentages(inventory: dict, total_quantity: int) -> None:
    for item in inventory.keys():
        percentage = round((inventory[item] / total_quantity) * 100, 1)
        print(f"Item {item} represents {percentage}%")


def get_abundant_items(inventory: dict, order: list) -> tuple[str, str]:
    most_item = order[0]
    least_item = order[0]

    for item in order[1:]:
        if inventory[item] > inventory[most_item]:
            most_item = item
        if inventory[item] < inventory[least_item]:
            least_item = item

    return most_item, least_item


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory, order = parse_inventory()

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    if len(inventory) > 0 and total_quantity > 0:
        print_percentages(inventory, total_quantity)

        most, least = get_abundant_items(inventory, order)
        print(f'Item most abundant: {most} with quantity', inventory[most])
        print(f'Item least abundant: {least} with quantity', inventory[least])

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()

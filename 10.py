def add(item, quantity, items):
    if item in items:
        items[item] += quantity
        print(f"UPDATED Item {item}")
    else:
        items[item] = quantity
        print(f"ADDED Item {item}")
    return items


def delete(item, quantity, items):
    if item in items:
        if items[item] >= quantity:
            items[item] -= quantity
            print(f"DELETED Item {item}")
        else:
            print(f"Item {item} could not be DELETED")
    else:
        print(f"Item {item} does not exist")
    return items


for _ in range(int(input())):
    items = {}
    for i in range(int(input())):
        item, quantity = input().split()
        items[item] = int(quantity)
    operations = [input().split() for i in range(int(input()))]
    for operation in operations:
        if operation[0] == "ADD":
            items = add(operation[1], int(operation[2]), items)
        else:
            items = delete(operation[1], int(operation[2]), items)
    print(f"Total Items in Inventory: {sum(items.values())}")

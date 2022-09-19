list = {}
for i in range(int(input())):
    for j in range(int(input())):
        arr = input().split()
        list[arr[0]] = int(arr[1])
    for j in range(int(input())):
        arr = input().split()
        name = arr[1]
        quantity = int(arr[2])
        if arr[0] == "ADD":
            if name in list:
                list[name] += quantity
                print("UPDATED Item " + name)
            else:
                list[name] = quantity
                print("ADDED Item " + name)
        else:
            if name not in list:
                print("Item " + name + " does not exist")
            else:
                if quantity > list[name]:
                    print("Item " + name + " could not be DELETED")
                else:
                    list[name] -= quantity
                    print("DELETED Item " + name)
print(f"Total Items in Inventory: {sum(list.values())}")

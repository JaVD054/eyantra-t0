for _ in range(int(input())):
    for i in range(int(input()), 0, -1):
        print("".join(["#" if (j + 1) % 5 == 0 else "*" for j in range(i)]))

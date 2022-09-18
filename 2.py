for _ in range(int(input())):
    print("\n3 ", end=" ")
    for i in range(1, int(input())):
        print(i**2 if i % 2 == 1 else i * 2, end=" ")

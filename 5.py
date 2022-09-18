for _ in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    print(" ".join(map(str, lis[-1::-1])))
    print(" ".join(map(lambda a: str(a + 3), lis[3::3])))
    print(" ".join(map(lambda a: str(a - 7), lis[5::5])))
    print(sum(lis[3:8]))

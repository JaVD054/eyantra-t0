from functools import reduce

for _ in range(int(input())):
    results = []
    for i in range(int(input())):
        results.append(input().split())
    print(reduce(lambda n1, n2: n1 if float(n1[1]) > float(n2[1]) else n2, results)[0])

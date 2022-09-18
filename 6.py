for _ in range(int(input())):
    words = input()[1:].split()
    print(",".join([str(len(word)) for word in words]))

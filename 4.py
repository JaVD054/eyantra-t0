from math import sqrt


def compute_distance(x1, y1, x2, y2):
    print(f"Distance: {sqrt((x1-x2)**2+(y1-y2)**2):.2f}")


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        x1, y1, x2, y2 = list(map(int, input().split()))
        compute_distance(x1, y1, x2, y2)

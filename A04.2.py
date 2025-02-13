import math

def count_squares(a, b):
    return max(0, math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)

for _ in range(int(input())):
    print(count_squares(*map(int, input().split())))
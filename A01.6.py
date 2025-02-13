import math

def distance(p1, p2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2)))

points = [tuple(map(int, input(f"Enter point {i+1} (x, y, z): ").split())) for i in range(10)]

neighbors = []
for i, p1 in enumerate(points):
    nearest = min((p2 for j, p2 in enumerate(points) if j != i), key=lambda p2: distance(p1, p2))
    neighbors.append((p1, nearest))

print(neighbors)

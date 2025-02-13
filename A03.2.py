import math

def is_fibonacci(n):
    return any(int(math.sqrt(x))**2 == x for x in (5*n*n + 4, 5*n*n - 4))

for _ in range(int(input())):
    print("IsFibo" if is_fibonacci(int(input())) else "IsNotFibo")
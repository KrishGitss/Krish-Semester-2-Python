def utopian_tree(n):
    return (1 << ((n + 1) // 2 + 1)) - 1 if n % 2 else (1 << (n // 2 + 1)) - 2

for _ in range(int(input())):
    print(utopian_tree(int(input())))
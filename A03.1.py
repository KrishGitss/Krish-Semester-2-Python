def digital_root(n):
    while n >= 10:
        n = sum(map(int, str(n)))
    return n

print(digital_root(45893))
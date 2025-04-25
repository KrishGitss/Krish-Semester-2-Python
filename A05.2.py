def max_chocolate_pieces(K):
    return (K // 2) * ((K + 1) // 2)

n = int(input().strip())
print("\n")

for _ in range(n):
    K = int(input().strip())
    print(max_chocolate_pieces(K))
    print("\n")
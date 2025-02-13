def min_operations_to_palindrome(s):
    return sum(abs(ord(s[i]) - ord(s[~i])) for i in range(len(s) // 2))

for _ in range(int(input())):
    print(min_operations_to_palindrome(input().strip()))
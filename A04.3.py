def is_pangram(s):
    return "Pangram" if set("abcdefghijklmnopqrstuvwxyz").issubset(s.lower()) else "Not Pangram"

print(is_pangram(input()))
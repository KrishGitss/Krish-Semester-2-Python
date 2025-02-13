Number = int(input("Enter a number: "))
RevNumber = 0


while(Number != 0):
    digit = Number % 10
    RevNumber = RevNumber * 10 + digit
    Number //= 10

print("Reversed number =" ,RevNumber,)
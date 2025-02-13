num = int(input("Enter Number Of Inputs: "))
numbers = [int(input("Enter Your Number: ")) for _ in range(num)]

for x in numbers:
    count = sum(1 for d in str(x) if d != '0' and x % int(d) == 0)
    print(count)
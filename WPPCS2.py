n = eval(input("Enter few numbers: "))
temp = 0

for i in range(0, len(n) // 2):
    temp = (n[i])
    n[i] = n[len(n) - 1 - i]
    n[len(n) - 1 - i] = temp
        
for i in range(0, len(n)):
    print(n[i])
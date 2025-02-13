import random 

randomnum = (random.choice([0, 1]) for i in range(0, 100))
maxzeros = 0
current = 0

for number in randomnum:
    if(number == 0):
        current += 1
        maxzeros = max(maxzeros, current)
    else:
        current = 0

print(maxzeros)
equivalence_classes = {0: [], 1: [], 2: [], 3: [], 4: []}

for num in range(1, 10001):
    remainder = num % 5
    equivalence_classes[remainder].append(num)

all_numbers = set(range(1, 10001))
union_of_classes = set()

for remainder in equivalence_classes:
    union_of_classes.update(equivalence_classes[remainder])

if all_numbers == union_of_classes:
    print("The equivalence classes are valid.")
else:
    print("There is an issue with the equivalence classes.")
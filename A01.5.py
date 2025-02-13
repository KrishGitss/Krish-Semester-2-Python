student_names = []

print("Enter the names of 10 students:")
for i in range(5):
    name = input(f"Student {i + 1}: ")[:15] 
    student_names.append(name)

print("\nReversed Student Names:")
for name in student_names:
    print(name[::-1])
conversions = {
    1: ("Inches", 12),
    2: ("Yards", 1/3),
    3: ("Miles", 1/5280),
    4: ("Millimeters", 304.8),
    5: ("Centimeters", 30.48),
    6: ("Meters", 0.3048),
    7: ("Kilometers", 0.0003048)
}

feet = float(input("Enter length in feet: "))

print("\nChoose a conversion option:")
for key, (unit, _) in conversions.items():
    print(f"{key}. Convert to {unit}")

choice = int(input("\nEnter your choice (1-7): "))
if choice in conversions:
    unit, factor = conversions[choice]
    print(f"{feet} feet is {feet * factor:.4f} {unit}")
else:
    print("Invalid choice! Please enter a number between 1 and 7.")

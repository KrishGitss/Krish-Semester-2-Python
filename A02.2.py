dictionary = {}

print("*PRODUCT DATABASE*")
while input("\nPress 1 to add a new entry, any other key to stop: ") == "1":
    product_name = input("Enter Product Name: ")
    dictionary[product_name] = float(input("Enter Price: "))

print("\n*DATABASE FINDER*")
while input("\nPress 1 to find an entry, any other key to stop: ") == "1":
    product_name = input("Enter Product Name: ")
    print(f"PRODUCT = {product_name}, PRICE = {dictionary.get(product_name, 'Not Found')}")
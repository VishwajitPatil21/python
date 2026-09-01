# Inventory Catalog Manager

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]

item = input("Enter product name to search: ")

if item in products:
    index = products.index(item)
    print("Product found!")
    print("Product:", item)
    print("Index location:", index)
else:
    print("Product not found in inventory.")
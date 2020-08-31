products = {}

while True:
    line = input().split(": ")
    if line[0] == "statistics":
        break
    product = line[0]
    qty = int(line[1])
    if product not in products:
        products[product] = 0
    products[product] += qty

print("Products in stock:")
for (product, qty) in products.items():
    print(f"- {product}: {qty}")

print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")

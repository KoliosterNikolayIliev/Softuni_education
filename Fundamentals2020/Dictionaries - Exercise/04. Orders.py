total_qty = {}
all_price = {}
line = ""
while True:
    line = input().split(" ")

    key = line[0]
    if key == "buy":
        break
    price = float(line[1])
    qty = int(line[2])
    if key not in all_price:
        all_price[key] = 0
    all_price[key] = price
    if key not in total_qty:
        total_qty[key] = 0
    total_qty[key] += qty

for (key, price) in all_price.items():
    total_sum = price * total_qty[key]
    print(f"{key} -> {total_sum:.2f}")

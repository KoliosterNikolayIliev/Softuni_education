list_of_items = input().split("|")
budget = float(input())
sold_items = []
bought_items = []

for i in range(len(list_of_items)):
    token = list_of_items[i].split("->")
    item = token[0]
    price = float(token[1])
    if item == "Clothes":
        max_price = 50.00
        if budget >= price:
            if price <= max_price:
                budget -= price
                new_price = f"{(price * 1.4):.2f}"
                sold_items.append(str(new_price))
                bought_items.append(price)

    elif item == "Shoes":
        max_price = 35.00
        if budget >= price:
            if price <= max_price:
                budget -= price
                new_price = f"{(price * 1.4):.2f}"
                sold_items.append(str(new_price))
                bought_items.append(price)

    elif item == "Accessories":
        max_price = 20.50
        if budget >= price:
            if price <= max_price:
                budget -= price
                new_price = f"{(price * 1.4):.2f}"
                sold_items.append(str(new_price))
                bought_items.append(price)

profit = sum([float(x) for x in sold_items]) - sum(bought_items)
print(' '.join([str(x) for x in sold_items]))
print(f"Profit: {profit:.2f}")

if sum([float(x) for x in sold_items]) + budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")

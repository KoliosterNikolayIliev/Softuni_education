items = input().split('|')
budget = float(input())

markup = []
profit = []
new_price = []

new_budget = 0
ticket = 150

for i in range(0, len(items)):
    item_type = str(items[i]).split('->')

    if str(item_type[0]) == 'Clothes':
        if 50 >= float(item_type[1]) <= budget > 0:
            budget = budget - float(item_type[1])
            markup.append(1.40 * float(item_type[1]))
            profit.append(1.40 * float(item_type[1]) - float(item_type[1]))

    if str(item_type[0]) == 'Shoes':
        if 35 >= float(item_type[1]) <= budget > 0:
            budget = budget - float(item_type[1])
            markup.append(1.40 * float(item_type[1]))
            profit.append(1.40 * float(item_type[1]) - float(item_type[1]))

    if str(item_type[0]) == 'Accessories':
        if 20.50 >= float(item_type[1]) <= budget > 0:
            budget = budget - float(item_type[1])
            markup.append(1.40 * float(item_type[1]))
            profit.append(1.40 * float(item_type[1]) - float(item_type[1]))

profit = sum(profit)
profit = round(profit, 2)
new_budget = sum(markup) + budget
new_budget = round(new_budget, 2)

for j in markup:
    j = round(j, 2)
    j = str(j)
    new_price.append(j)


print(" ".join(new_price))
print(f'Profit: {profit}')
if new_budget >= ticket:
    print("Hello, France!")
else:
    print("Time to go.")

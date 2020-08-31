import re

pattern = r'^>>([a-zA-Z]+)<<([0-9]+\.?[0-9]+)!([0-9]+)$'
furniture = []
total_money = 0
line = input()

while line != "Purchase":
    match = re.match(pattern, line)
    if match:
        name = match.group(1)
        price = float(match.group(2))
        quantity = int(match.group(3))

        furniture.append(name)
        total_money += price * quantity
    line = input()

print(f"Bought furniture:")
[print(x) for x in furniture]
print(f"Total money spend: {total_money:.2f}")

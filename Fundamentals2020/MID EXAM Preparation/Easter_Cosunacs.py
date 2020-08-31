budget = float(input())
flour1kg = float(input())
egg_price = flour1kg * 0.75
milk_1l = 1.25 * flour1kg

one_coz_price = flour1kg + egg_price + 0.25 * milk_1l
coz_count = 0
colored_eggs = 0
moneyLeft = 0
while budget > one_coz_price:
    coz_count += 1
    budget -= one_coz_price
for i in range(1, coz_count + 1):
    colored_eggs += 3
    if i % 3 == 0:
        colored_eggs -= (i - 2)

print(f"You made {coz_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

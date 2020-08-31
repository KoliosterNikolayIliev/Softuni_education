budget = float(input())
flower_price = float(input())

eggs_price = 0.75 * flower_price
milk_price = (1.25 * flower_price) * 0.25

count_cozunacs = 0
one_cozunac_price = flower_price + eggs_price + milk_price
coloured_eggs = 0
money_left=budget
while money_left >= one_cozunac_price:
    money_left -= one_cozunac_price
    count_cozunacs += 1
    coloured_eggs += 3
    if count_cozunacs % 3 == 0:
        coloured_eggs -= (count_cozunacs - 2)

print (f"You made {count_cozunacs} cozonacs! Now you have {coloured_eggs} eggs and {money_left:.2f}BGN left.")


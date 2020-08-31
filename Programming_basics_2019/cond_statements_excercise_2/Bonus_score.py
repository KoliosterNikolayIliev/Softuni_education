number = int(input())
bonus = 0
if number <= 100:
    bonus = 5

elif number > 100 and number<1000:
    bonus = 0.2 * number

else:
    number > 1000
    bonus = number * 0.1

if number % 2 == 0:
    bonus=bonus+1

elif number % 10 == 5:
    bonus = bonus + 2

number=number+bonus

print(bonus)
print(number)
number = input()


def odd_even_sum(num):
    even_sum = 0
    odd_sum = 0
    for i in num:
        if int(i) % 2 == 0:
            even_sum += int(i)
        else:
            odd_sum += int(i)
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


print(odd_even_sum(number))

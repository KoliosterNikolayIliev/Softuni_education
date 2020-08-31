def perfect_number(number):
    messages = []
    sum_divider = 0
    for i in range(1, number):
        if number % i == 0:
            sum_divider += i

    if number == sum_divider:
        messages.append("We have a perfect number!")
    else:
        messages.append("It's not so perfect.")
    return messages


number = int(input())
# print('\n'.join(perfect_number(number)))
print(perfect_number(number))

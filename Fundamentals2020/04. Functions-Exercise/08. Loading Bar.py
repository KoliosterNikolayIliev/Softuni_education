def loading(percentage):
    message = []
    percentage_loading = '[..........]'
    for i in range(10, percentage + 10, 10):
        i //= i
        percentage_loading = percentage_loading.replace('.', '%', i)
    if percentage < 100:
        message.append(f'{percentage}% {percentage_loading}')
        message.append('Still loading...')
    else:
        message.append('100% Complete!')
        message.append(f'{percentage_loading}')

    return message


percentage = int(input())
print('\n'.join(loading(percentage)))
# number = '[..........]'
# string.replace(old, new, count)
# new_number=number.replace('.', '%', 3)
# print(new_number)

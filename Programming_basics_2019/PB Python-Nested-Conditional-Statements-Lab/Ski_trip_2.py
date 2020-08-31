days = int(input())
room_type = input()
evaluation = input()

nights = days - 1

discount = 0
price = 0

if room_type == 'apartment':
    price = 25
    if nights < 10:
        discount = 0.3
    elif 10 <= nights <= 15:
        discount = 0.35
    elif nights > 15:
        discount = 0.50
elif room_type == 'president apartment':
    price = 35
    if nights < 10:
        discount = 0.1
    elif 10 <= nights <= 15:
        discount = 0.15
    elif nights > 15:
        discount = 0.20
elif room_type == 'room for one person':
    price = 18
total_sum = nights * price
total_sum = total_sum - (total_sum * discount)

if evaluation == 'positive':
    total_sum = total_sum + (total_sum * 0.25)
    print(f'{total_sum:.2f}')

if evaluation == 'negative':
    total_sum = total_sum - (total_sum * 0.10)
    print(f'{total_sum:.2f}')

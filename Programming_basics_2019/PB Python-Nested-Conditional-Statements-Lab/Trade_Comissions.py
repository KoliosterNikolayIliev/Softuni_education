city = input()
sales = float(input())

bonus = -1
if city == 'Sofia':
    if 0 <= sales <= 500:
        bonus = 0.05 * sales
    elif 500 < sales <= 1000:
        bonus = 0.07 * sales
    elif 1000 < sales <= 10000:
        bonus = 0.08 * sales
    elif sales > 10000:
        bonus = 0.12 * sales

elif city == 'Varna':
    if 0 <= sales <= 500:
        bonus = 0.045 * sales
    elif 500 < sales <= 1000:
        bonus = 0.075 * sales
    elif 1000 < sales <= 10000:
        bonus = 0.10 * sales
    elif sales > 10000:
        bonus = 0.13 * sales

elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        bonus = 0.055 * sales
    elif 500 < sales <= 1000:
        bonus = 0.08 * sales
    elif 1000 < sales <= 10000:
        bonus = 0.12 * sales
    elif sales > 10000:
        bonus = 0.145 * sales
if bonus>=0:
    print(f'{bonus:.2f}')
else: print ('error')
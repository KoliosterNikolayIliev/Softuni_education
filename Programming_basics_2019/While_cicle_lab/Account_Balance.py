installment_count = int(input())

counter = 0
total = 0
while counter < installment_count:

    counter += 1
    installment = float(input())
    if installment < 0:
        print('Invalid operation!')
        break
    total += installment
    print(f'Increase: {installment:.2f}')


print(f'Total: {total:.2f}')

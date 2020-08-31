goal = 0

while True:
    steps_count = input()
    if steps_count == 'Going home':
        steps_count = int(input())
        goal += steps_count
        if goal >= 10000:
            print('Goal reached! Good job!')
            break
        else:
            print(f'{10000 - goal} more steps to reach goal.')
            break
    else:
        steps_count = int(steps_count)
        goal += steps_count

    if goal >= 10000:
        print('Goal reached! Good job!')
        break

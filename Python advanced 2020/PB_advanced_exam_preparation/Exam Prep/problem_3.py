def list_manipulator(list_of_numbers, *args):
    ll = list_of_numbers
    command1 = args[0]
    command2 = args[1]
    numbers = []
    if len(args) > 2:
        for i in range(2, len(args)):
            numbers.append(args[i])

    if numbers:
        if command1 == 'add' and command2 == 'beginning':
            while numbers:
                ll.insert(0, numbers.pop())
        elif command1 == 'add' and command2 == 'end':
            numbers = list(reversed(numbers))
            while numbers:
                ll.append(numbers.pop())
        elif command1 == 'remove' and command2 == 'beginning':
            for i in range(numbers[0]):
                ll.remove(ll[0])
        elif command1 == 'remove' and command2 == 'end':
            for i in range(numbers[0]):
                ll.pop()
    else:
        if command1 == 'remove' and command2 == 'beginning':
            ll.remove(ll[0])
        elif command1 == 'remove' and command2 == 'end':
            ll.pop()

    return ll


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))

name = input()

if name != 'Johnny':
    print(f'Hello, {name}!')
    while not name == 'Johnny':
        name = input()
        if name == 'Johnny':
            print('Hello, my love!')
        else:
            print(f'Hello, {name}!')

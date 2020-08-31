command=input()

tokens = command.split()
if tokens[0] == 'exchange':
    index = int(tokens[1])
    kur=tokens[0]

    print(index)
    print(kur)
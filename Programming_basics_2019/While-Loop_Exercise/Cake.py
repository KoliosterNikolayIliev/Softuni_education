a = int(input())
b = int(input())


cake = a * b
cake_left = True
piece = input()

while not piece == 'STOP':

    piece = int(piece)
    cake -= piece
    if cake < 0:
        cake_left = False
        break
    piece = input()
if cake_left:
    print(f'{cake} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cake)} pieces more.')

a = int(input())
b = int(input())
c = int(input())

volume = a * b * c
has_volume = True
box = input()

while not box == 'Done':

    box = int(box)
    volume -= box
    if volume < 0:
        has_volume = False
        break
    box = input()
if has_volume:
    print(f'{volume} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(volume)} Cubic meters more.')


animals = input().split(', ')
if animals[len(animals) - 1] == "wolf":
    print('Please go away and stop eating my sheep')
else:
    counter = 1
    stop = False
    for i in range(len(animals) - 1, 0, -1):
        if not stop:
            curr = animals[i]
            prev = animals[i - 1]
            if curr == "sheep" and prev == "wolf":
                print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")
                stop = True
            counter += 1
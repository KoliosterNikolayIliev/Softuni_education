import math

change = float(input())
change *= 100
change=math.floor(change)
counter = 0

while change > 0:
    if change / 200 >= 1:
        counter += 1
        change -= 200
    else:
        if change / 100 >= 1:
            counter += 1
            change -= 100
        else:
            if change / 50 >= 1:
                counter += 1
                change -= 50
            else:
                if change / 20 >= 1:
                    counter += 1
                    change -= 20
                else:
                    if change / 10 >= 1:
                        counter += 1
                        change -= 10
                    else:
                        if change / 5 >= 1:
                            counter += 1
                            change -= 5
                        else:
                            if change / 2 >= 1:
                                counter += 1
                                change -= 2
                            else:
                                if change / 1 >= 1:
                                    counter += 1
                                    change -= 1



print(counter)

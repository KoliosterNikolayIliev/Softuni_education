speed = float(input())

if speed <= 10:
    speed = 'slow'
elif speed > 10 and speed <= 50:
    speed = 'average'
elif speed > 50 and speed <= 150:
    speed = 'fast'
elif speed > 150 and speed <= 1000:
    speed = 'ultra fast'
elif speed > 1000:
    speed = 'extremely fast'

print(speed)


n = int(input())
max_value = 0
output = ''
for i in range(n):
    snow = int(input())
    time = int(input())
    quality = int(input())
    value = (snow // time) ** quality
    if value > max_value:
        max_value = value
        output = f'{snow} : {time} = {max_value} ({quality})'
print(output)
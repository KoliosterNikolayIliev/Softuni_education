numbers_list = list(map(lambda x: int(x), input().split(' ')))
number = int(input())

for i in range(number):
    element = 0
    for j in range(len(numbers_list)):
        element = min(numbers_list)
    numbers_list.remove(element)

print(numbers_list)

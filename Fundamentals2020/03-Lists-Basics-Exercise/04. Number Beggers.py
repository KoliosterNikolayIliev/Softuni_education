numbers_as_str = input().split(', ')
numbers_list = list(map(lambda x: int(x), numbers_as_str))
beggars = int(input())
beggars_list = [0] * beggars

for i in range(len(numbers_list)):
    element = numbers_list[i]
    beggar_index = i % len(beggars_list)
    beggars_list[beggar_index] += element

print(beggars_list)

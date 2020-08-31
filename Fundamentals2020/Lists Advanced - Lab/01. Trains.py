wagons = int(input())
command = input().split()
my_list = []
for i in range(wagons):
    my_list.append(0)
last_wagon = []
while not command[0] == 'End':
    if command[0] == 'add':
        num = int(command[1])
        last_wagon.append(num)

    elif command[0] == 'insert':
        my_list.pop(int(command[1]))
        my_list.insert(int(command[1]), int(command[2]))

    elif command[0] == 'leave':
        index = int(command[1])
        num = int(my_list[index]) - int(command[2])
        my_list.pop(index)
        my_list.insert(index, num)

    command = input().split()
k = 0
for j in last_wagon:
    k += j
index = wagons - 1
num = int(my_list[index]) + k
my_list.pop(index)
my_list.insert(index, num)

print(my_list)

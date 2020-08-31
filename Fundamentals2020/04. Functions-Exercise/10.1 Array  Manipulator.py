import sys


def read_number_list():
    input_arr = input().split()
    nums = []

    for i in input_arr:
        nums.append(int(i))

    return nums


def exchange(nums, index):
    new_list = []
    for i in range(index + 1, len(nums)):
        new_list.append(nums[i])

    for i in range(index + 1):
        new_list.append(nums[i])

    return new_list


def max_number_index(nums, type):
    max_num = -sys.maxsize
    max_num_index = -1

    if type == 'even':
        for i in range(len(nums)):
            num = nums[i]
            if num % 2 == 0 and num >= max_num:
                max_num = num
                max_num_index = i
    else:
        for i in range(len(nums)):
            num = nums[i]
            if num % 2 != 0 and num >= max_num:
                max_num = num
                max_num_index = i

    return max_num_index


def min_number_index(nums, type):
    min_num = -sys.maxsize
    min_num_index = -1

    if type == 'even':
        for i in range(len(nums)):
            num = nums[i]
            if num % 2 == 0 and num <= min_num:
                min_num = num
                min_num_index = i
    else:
        for i in range(len(nums)):
            num = nums[i]
            if num % 2 != 0 and num <= min_num:
                min_num = num
                min_num_index = i

    return min_num_index


def firs_elements(nums, count, type):
    elements = []

    if type == 'even':
        for num in nums:
            if num % 2 == 0 and len(elements) < count:
                elements.append(num)
    else:
        for num in nums:
            if num % 2 != 0 and len(elements) < count:
                elements.append(num)

    return elements


def solve():
    nums = read_number_list()

    command_input = input()
    while command_input != 'end':
        args = command_input.split()
        command = args[0]

        if command == 'exchange':
            index = int(args[1])

            if len(nums) <= index < 0:
                print('Invalid index')
                command_input = input()
                continue

            nums = exchange(nums, index)
        elif command == 'max':
            type = args[1]
            max_index = max_number_index(nums, type)

            if max_index != -1:
                print(max_index)
            else:
                print('No matches')
        elif command == 'min':
            type = args[1]
            min_index = min_number_index(nums, type)

            if min_index != -1:
                print(min_index)
            else:
                print('No matches')
        elif command == 'first':
            count = int(args[1])
            type = args[2]

            if count > len(nums):
                print('Invalid count')
                command_input = input()
                continue
            print(firs_elements(nums,count,type))

        command_input = input()


solve()

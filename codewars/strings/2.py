def binary_array_to_number(arr: list):
    rev = arr[::-1]
    result = 0
    for i in range(len(rev)):
        result += rev[i] * 2 ** (i - 1)
    return int(result*2)


arr = [1,0,0,0,0,0,0,0,0]
print(binary_array_to_number(arr))

arr2 = [0,0,1,0]
print(binary_array_to_number(arr2))

arr3 = [1,1,1,1]
print(binary_array_to_number(arr3))

arr4 = [0,1,1,0]
print(binary_array_to_number(arr4))
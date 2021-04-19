# filtering

# arr = [1, 2, 3, 4, 5, 6]
#
# arr2 = [x for x in arr if x % 2 == 0]
#
# print(arr2)
#
# arr3 = list(filter(lambda x: x % 2 == 0, arr))
# print(arr3)
#
#
# def if_even(x):
#     if x % 2 == 0:
#         return x
#
# arr4 = list(filter(if_even, arr))
# print(arr4)

# SETS

# a_set = {1, 2, 3, 3}
# print(a_set)

# b_set = {10, 12, 58, 3, 4}
# a = {x for x in range(10)}
# print(a)
# print(a_set.union(b_set))
# print(a_set.symmetric_difference(b_set))
# print(a_set.difference(b_set))
# print(b_set.difference(a_set))
# print(a_set.intersection(b_set))

z = complex(2, 10)
print(z.real)
print(z.imag)
print(isinstance(z, complex))


# from Crypto.Util import number
# from sympy.ntheory import factorint
#
# import timeit
# import numpy as np
# import matplotlib.pyplot as plt
#
# bits = list(range(10,90,10))
#
#
# def create_random_numbers(bit):
#     numbers = []
#     random_integer = number.getRandomNBitInteger(bit)
#     numbers.append(random_integer)
#     return numbers
#
#
# def create_factors(numbers):
#     factors = []
#     for i in numbers:
#         factors.append(factorint(i))
#     return factors
#
#
# def from_factors_to_num_list(factors):
#     nums = []
#     for f in factors:
#         n = [k ** v for k, v in f.items()]
#         result = 1
#         for x in n:
#             result = result * x
#         nums.append(result)
#     return nums
#
#
# create_factors_time_setup_code = '''
# from Crypto.Util import number
# from sympy.ntheory import factorint
# import timeit
# from __main__  import create_factors
# from __main__ import create_random_numbers
# numbers = create_random_numbers({})
# '''
#
# create_factors_time_function = '''
# create_factors(numbers)
#     '''
#
# from_factors_to_num_list_time_setup_code = '''
# from Crypto.Util import number
# from sympy.ntheory import factorint
# import timeit
# from __main__  import create_factors
# from __main__ import create_random_numbers
# from __main__ import from_factors_to_num_list
# numbers = create_random_numbers({})
# factors = create_factors(numbers)
# '''
#
# from_factors_to_num_list_time_function = '''
# from_factors_to_num_list(factors)
#
#     '''
#
#
# def time_measure(setup_code, function, bit):
#     SETUP_CODE = setup_code.format(bit)
#
#     TEST_CODE = function
#     times = timeit.repeat(setup=SETUP_CODE,
#                           stmt=TEST_CODE,
#                           number=5)
#     return min(times)
#
#
# times_create_factors = []
# times_from_factors_to_nums = []
# for bit in bits:
#     times_create_factors.append(time_measure(create_factors_time_setup_code, create_factors_time_function, bit))
#     times_from_factors_to_nums.append(
#         time_measure(from_factors_to_num_list_time_setup_code, from_factors_to_num_list_time_function, bit))
# print(times_create_factors)
# print(times_from_factors_to_nums)
#
#
# def plot_time_function(bits, times_create_factors, times_from_factors_to_nums):
#     plt.plot(bits, times_create_factors, 3000, c='green',marker='o')
#     plt.plot(bits, times_from_factors_to_nums, 3000, c='red', marker='o')
#     plt.axis([min(bits), max(bits)+10, min(times_from_factors_to_nums), max(times_create_factors)])
#     plt.xlabel("number of bits")
#     plt.ylabel("time")
#     return plt.show()
#
#
# plot_time_function(bits, times_create_factors, times_from_factors_to_nums)

# a =["John", "Charles", "Mike"]
# b = ["Jenny", "Christy", "Monica"]
#
# x = zip(a, b)
#
# #use the tuple() function to display a readable version of the result:
#
# print([list(x) for x in x])

a = (x for x in range(10))
print([x for x in a])
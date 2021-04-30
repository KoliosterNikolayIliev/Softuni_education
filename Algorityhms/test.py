from Crypto.Util import number
from sympy.ntheory import factorint

import timeit
import numpy as np
import matplotlib.pyplot as plt

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

# Write your code here

# import time
# from numpy.random import rand
#
#
# def exec_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         return (end - start)
#
#     return wrapper
#
#
# @exec_time
# def py_time(randoms):
#     return sum(randoms)
#
#
# @exec_time
# def np_time(randoms):
#     return np.sum(randoms)
#
#
# py_times = []
# np_times = []
#
#
# n = np.array([el for el in range(0, 1000000, 50000)])
# for j in n:
#     randoms = rand(j)
#     py_10_loop = []
#     np_10_loop = []
#     for i in range(10):
#         py_10_loop.append(py_time(randoms))
#         np_10_loop.append(np_time(randoms))
#     py_times.append(np.mean(py_10_loop))
#     np_times.append(np.mean(np_10_loop))
#
#
# def plot_time_function(bits, times_create_factors, times_from_factors_to_nums):
#     plt.plot(bits, times_create_factors, 3000, c='green')
#     plt.plot(bits, times_from_factors_to_nums, 3000, c='red', )
#     plt.axis([min(bits), max(bits)+10, min(times_from_factors_to_nums), max(times_create_factors)])
#     plt.xlabel("array length")
#     plt.ylabel("time")
#     return plt.show()
#
# plot_time_function(n, py_times, np_times)


# def get_limit(f, a):
#     epsilon = np.array([10 ** p for p in np.arange(0, -11, -1, dtype=float)])
#     x = np.append(a - epsilon, (a + epsilon)[::-1])
#     y = f(x)
#     return y
#
#
# print(get_limit(lambda x: x ** 2, 3))
# print(get_limit(lambda x: x ** 2 + 3 * x, 2))
# print(get_limit(lambda x: np.sin(x), 0))

# finding local minimum of function
x_old = 0
x_new = 6
step_size = 0.01
precision = 1E-5  # (0.00001)


def df(x):
    # f`(x^4 - 3x^3 +2) = 4x^3-9x^2
    y = 4 * x ** 3 - 9 * x ** 2
    return y


while abs(x_new - x_old) > precision:
    x_old = x_new
    x_new -= step_size * df(x_old)

print(f'The local minimum occurs at {x_new}')

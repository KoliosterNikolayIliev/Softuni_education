import copy
from datetime import date
from functools import reduce

from Crypto.Util import number
from sympy.ntheory import factorint

from time import time
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
# x_old = 0
# x_new = 6
# step_size = 0.01
# precision = 1E-5  # (0.00001)
#
#
# def df(x):
#     # f`(x^4 - 3x^3 +2) = 4x^3-9x^2
#     y = 4 * x ** 3 - 9 * x ** 2
#     return y
#
#
# while abs(x_new - x_old) > precision:
#     x_old = x_new
#     x_new -= step_size * df(x_old)
#
# print(f'The local minimum occurs at {x_new}')

#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # a class method to create a Person object by birth year.
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)
#
#     # a static method to check if a Person is adult or not.
#     @staticmethod
#     def isAdult(age):
#         return age > 18
#
#
# person1 = Person('mayank', 21)
# person2 = Person.fromBirthYear('mayank', 1996)
#
# print(person1.age)
# print(person2.age)
#
# # print the result
# print(Person.isAdult(22))

# def pig_it(text):
#     words = text.split(' ')
#     new_words = []
#     for word in words:
#         if word not in [chr(x) for x in range(33, 64)]:
#             word = word[1:] + word[0] + 'ay'
#         new_words.append(word)
#     return ' '.join(new_words)
#
#
# pig_it('kur')
#
#
# def pig_it_codewars(text):
#     lst = text.split()
#     return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])


# def determinant(matrix, total=0):
#     indices = list(range(len(matrix)))
#
#     if len(matrix) == 1 and len(matrix[0]) == 1:
#         return 1
#
#     if len(matrix) == 2 and len(matrix[0]) == 2:
#         val = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
#         return val
#
#     for fc in indices:
#         As = copy.deepcopy(matrix)
#         As = As[1:]
#         height = len(As)
#
#         for i in range(height):
#             As[i] = As[i][0:fc] + As[i][fc + 1:]
#
#         sign = (-1) ** (fc % 2)
#         sub_det = determinant(As)
#         total += sign * matrix[0][fc] * sub_det
#
#     return total
#
# def determinant(m):
#     a = 0
#     if len(m) == 1:
#         a = m[0][0]
#     else:
#         for n in range(len(m)):
#             if (n + 1) % 2 == 0:
#                 a -= m[0][n] * determinant([o[:n] + o[n+1:] for o in m[1:]])
#             else:
#                 a += m[0][n] * determinant([o[:n] + o[n+1:] for o in m[1:]])


# def scramble(s1, s2):
#     for letter in s2:
#         if s1.count(letter)< s2.count(letter):
#             return False
#         if letter not in s1:
#             return False
#     return True

# def scramble(s1, s2):
#     d2 = {}
#     d1 = {}
#     for letter in s2:
#         d1[letter] = 0
#         if letter not in d2.keys():
#             d2[letter] = 1
#         else:
#             d2[letter] += 1
#     for letter in s1:
#         if letter not in d1.keys():
#             continue
#         else:
#             if d1[letter] == d2[letter]:
#                 continue
#             else:
#                 d1[letter] += 1
#     return d1 == d2

from collections import Counter
def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2)- Counter(s1)) == 0

print(scramble('scriptjavx', 'javascript'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
print(scramble('scriptjava', 'javascript'))
print(scramble('scriptingjava', 'javascript'))

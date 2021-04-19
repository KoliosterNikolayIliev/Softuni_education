# for number in range(1, 9 + 1):
#     with open(f'file{number}.txt', "a"):
#         pass

import glob
import re

text_files = glob.glob("*.txt")
lists = []
for text_file in text_files:
    with open(text_file) as file:
        lists.append(file.readlines())

all_lines = sum(lists, [])

matches = [re.compile('[0-9]+\.*[0-9]*').search(line) for line in all_lines]

numbers = [float(match.group(0)) for match in matches if match]
print(numbers)
numbers_bellow_60 = [number for number in numbers if number < 70]
print(f'под 60 год:{numbers_bellow_60} бр.{len(numbers_bellow_60)}')
numbers = [number for number in numbers if 105 > number > 20]
print(numbers)
print(sum(numbers) / len(numbers))
print(f'брой {len(numbers)}')

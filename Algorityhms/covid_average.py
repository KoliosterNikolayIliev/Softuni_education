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
print([number for number in numbers if 30>number>1])
numbers = [number for number in numbers if 105 > number > 20]
print([number for number in numbers if 40>number>10])
print(len([number for number in numbers if 40>number>10]))

numbers_bellow_60_above_50 = [number for number in numbers if 50< number <= 60]
print(f'под 60 год:{numbers_bellow_60_above_50} \n бр.{len(numbers_bellow_60_above_50)}')

numbers_bellow_50 = [number for number in numbers if number <= 50]
print(f'под 50 год:{numbers_bellow_50} \n бр.{len(numbers_bellow_50)}')

numbers_above_70 = [number for number in numbers if number >= 70]
print(f'над 70 год:{numbers_above_70} \n бр.{len(numbers_above_70)}')

print(sum(numbers) / len(numbers))
print(f'брой {len(numbers)}')

n = int(input())
even_set = set()
odd_set = set()

for i in range(1, n+1):
    name = input()
    ascii_sum = sum([ord(x) for x in name]) // i

    if ascii_sum % 2 == 0:
        even_set.add(ascii_sum)
    else:
        odd_set.add(ascii_sum)
sum_even_set = sum(even_set)
sum_odd_set = sum(odd_set)

if sum_even_set == sum_odd_set:
    union_values = list(odd_set.union(even_set))
    print(f"{', '.join([str(x) for x in union_values])}")
if sum_even_set < sum_odd_set:
    different_values = list(odd_set.difference(even_set))
    print(f"{', '.join([str(x) for x in different_values])}")
if sum_even_set > sum_odd_set:
    symmetric_different_values = list(odd_set.symmetric_difference(even_set))
    print(f"{', '.join([str(x) for x in symmetric_different_values])}")



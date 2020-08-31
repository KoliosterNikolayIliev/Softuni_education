numbers = list(map(float, input().split()))

nums_and_occurances = {}
for num in numbers:
    if num not in nums_and_occurances:
        nums_and_occurances[num] = 0
    nums_and_occurances[num] +=1

[print(f"{k} - {v} times") for k, v in nums_and_occurances.items()]

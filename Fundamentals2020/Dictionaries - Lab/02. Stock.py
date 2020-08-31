stock = input().split(" ")
items = input().split(" ")
dictionary = {}
for i in range(0, len(stock), 2):
    key = stock[i]
    value = stock[i + 1]
    dictionary[key] = int(value)

for i in range(len(items)):
    if items[i] in dictionary.keys():
        print(f"We have {dictionary[items[i]]} of {items[i]} left")
    else:
        print(f"Sorry, we don't have {items[i]}")

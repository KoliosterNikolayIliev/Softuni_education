items = input().split(" ")
dictionary = {}
for i in range(0, len(items), 2):
    key = items[i]
    value = items[i + 1]
    dictionary[key] = int(value)
print(dictionary)

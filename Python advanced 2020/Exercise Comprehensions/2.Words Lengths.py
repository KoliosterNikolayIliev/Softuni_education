strings = [x for x in input().split(", ")]
dictionary = {name: len(name) for name in strings}
print(', '.join([f"{k} -> {v}" for k, v in dictionary.items()]))

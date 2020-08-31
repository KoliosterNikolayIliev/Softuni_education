word = input()
strings = {}
for char in word:
    if char != " ":
        if char not in strings:
            strings[char] = 0
        strings[char] += 1
for (char, value) in strings.items():
    print(f"{char} -> {strings[char]}")

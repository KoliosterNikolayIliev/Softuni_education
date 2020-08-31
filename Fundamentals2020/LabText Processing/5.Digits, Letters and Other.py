string = input()
letters = ""
digits = ""
other = ""
for i in string:
    if i.isalpha():
        letters += i
    elif i.isdigit():
        digits += i
    else:
        other += i

print(digits)
print(letters)
print(other)

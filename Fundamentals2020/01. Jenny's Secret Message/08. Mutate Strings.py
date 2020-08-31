str1 = input()
str2 = input()
previous = str1
for i in range(len(str1)):
    new_str = ''
    for j in range(i + 1):
        new_str += str2[j]
    for y in range(i + 1, len(str1)):
        new_str += str1[y]
    if new_str != previous:
        print(new_str)
        previous = new_str

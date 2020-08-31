strings = input().split(" ")
str1 = strings[0]
str2 = strings[1]
total_sum = 0
for i in range(max(len(str1), len(str2))):
    if i < len(str1) and i < len(str2):
        total_sum += ord(str1[i]) * ord(str2[i])
    else:
        if i < len(str1):
            total_sum += ord(str1[i])
        else:
            total_sum += ord(str2[i])

print(total_sum)

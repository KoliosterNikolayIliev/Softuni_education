list1 = input().split(", ")
list2 = input().split(", ")
list3 = []

for j in list1:
    if any(j in s for s in list2):
        list3.append(j)

print(list3)

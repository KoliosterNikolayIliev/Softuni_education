a = int(input())
b = int(input())
print('Before')
print(f"a = {a} \nb = {b}")
temp = a
a = b
b = temp
print('After')
print(f"a = {a} \nb = {b}")
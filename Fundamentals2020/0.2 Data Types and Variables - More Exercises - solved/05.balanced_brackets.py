
count = int(input())
balance = True
open = False

for i in range(0,count):
    data = input()
    if data == "(":
        if not open:
            open = True
        else:
            balance = False
    if data == ")":
        if open:
            open = False
        else:
            balance = False
if  balance and not open:
    print("BALANCED")
else:
    print("UNBALANCED")

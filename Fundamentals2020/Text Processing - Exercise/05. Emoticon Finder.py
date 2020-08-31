text = input()
lst = []
emoticons =[]
for i in text:
    lst.append(i)

for j in range(len(lst)):
    if lst[j] == ":":
        emoticons.append(lst[j]+lst[j+1])

print("\n".join(emoticons))

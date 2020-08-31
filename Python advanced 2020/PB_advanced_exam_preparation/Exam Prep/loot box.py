from collections import deque

box1 = deque([int(x) for x in input().split()])
lst = reversed([int(x) for x in input().split()])
box2 = deque(lst)
collection = []

while box1 and box2:
    item1 = box1.popleft()
    item2 = box2.popleft()
    sum_items = item1+item2
    if sum_items % 2 == 0:
        collection.append(sum_items)
    else:
        box1.appendleft(item1)
        box1.append(item2)
if box1:
    print("Second lootbox is empty")
else:
    print("First lootbox is empty")

value = sum(collection)
if value >= 100:
    print(f"Your loot was epic! Value: {value}")
else:
    print(f"Your loot was poor... Value: {value}")

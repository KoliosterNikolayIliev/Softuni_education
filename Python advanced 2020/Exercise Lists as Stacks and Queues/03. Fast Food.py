from _collections import deque

food_qty = int(input())
ord_str = input().split()
orders = deque()
for i in range(len(ord_str)):
    orders.append(int(ord_str[i]))

print(max(orders))

while orders:

    popped = orders.popleft()
    food_qty -= popped
    if food_qty < 0:
        orders.appendleft(popped)
        break

if not orders:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")

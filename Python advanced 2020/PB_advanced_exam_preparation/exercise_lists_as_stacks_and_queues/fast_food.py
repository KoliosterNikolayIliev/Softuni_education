from collections import deque

qty_of_food = int(input())

orders = deque([int(x) for x in input().split()])
print(max(orders))

while orders:
    order = orders.popleft()
    if order <= qty_of_food:
        qty_of_food -= order
    else:
        orders.appendleft(order)
        break
if orders:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")
else:
    print("Orders complete")

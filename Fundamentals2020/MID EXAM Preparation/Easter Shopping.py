shop_list = input().split(" ")
n = int(input())

for i in range(n):
    command = input().split(" ")
    cmd = command[0]
    if cmd == "Include":
        shop = command[1]
        shop_list.append(shop)
    elif cmd == "Visit":
        numberOfShops = int(command[2])
        pos = command[1]
        if 0 < numberOfShops <= len(shop_list):
            if pos == "first":
                del shop_list[0:numberOfShops]
            else:
                for k in range(0, numberOfShops):
                    shop_list.pop()
    elif cmd == "Prefer":
        shop_index_1 = int(command[1])
        shop_index_2 = int(command[2])
        if shop_index_1 in range(len(shop_list)) and shop_index_2 in range(len(shop_list)):
            shop_list[shop_index_2], shop_list[shop_index_1] = shop_list[shop_index_1], shop_list[shop_index_2]
    elif cmd == "Place":
        shop = command[1]
        shop_index = int(command[2])
        if (shop_index + 1) in range(len(shop_list)):
            shop_list.insert(shop_index + 1, shop)
print(f"Shops left: \n{' '.join(shop_list)}")

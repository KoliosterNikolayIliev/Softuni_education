clothes = [int(x) for x in input().split()]
rack = int(input())
for_rack = 0
list_of_racks = []
total = 0

while True:
    if clothes:
        rug = clothes.pop()
        for_rack += rug
        total += rug
        if for_rack == rack:
            list_of_racks.append(for_rack)
            for_rack = 0
        if for_rack > rack:
            clothes.append(rug)
            total -= rug
            for_rack -= rug
            list_of_racks.append(for_rack)
            for_rack = 0
    else:
        break
if sum(list_of_racks) < total:
    list_of_racks.append(total - sum(list_of_racks))
print(len(list_of_racks))


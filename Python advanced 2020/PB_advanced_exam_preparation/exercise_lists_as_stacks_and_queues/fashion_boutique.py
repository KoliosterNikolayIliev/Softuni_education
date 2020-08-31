stack_of_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
current_rack_capacity = rack_capacity

racks_counter = 1

while stack_of_clothes:
    clothe = stack_of_clothes.pop()
    if clothe <= current_rack_capacity:
        current_rack_capacity -= clothe
    else:
        stack_of_clothes.append(clothe)
        current_rack_capacity = rack_capacity
        racks_counter += 1
print(racks_counter)
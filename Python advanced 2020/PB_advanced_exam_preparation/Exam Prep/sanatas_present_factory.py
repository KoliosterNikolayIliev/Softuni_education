from collections import deque

toys = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
crafted_toys = []
materials = deque(reversed([int(x) for x in input().split()]))
magic_values = deque([int(x) for x in input().split()])

while True:
    if not materials or not magic_values:
        break
    material = materials[0]
    magic = magic_values[0]

    toy_magic = material * magic
    if toy_magic in toys:
        crafted_toys.append(toys[toy_magic])
        materials.popleft()
        magic_values.popleft()
    else:
        if toy_magic < 0:
            result = material + magic
            materials.popleft()
            magic_values.popleft()
            materials.appendleft(result)
        elif toy_magic > 0:
            magic_values.popleft()
            materials[0] += 15
        else:
            if material == 0:
                materials.popleft()

            if magic == 0:
                magic_values.popleft()


if "Teddy bear" in crafted_toys and "Bicycle" in crafted_toys or "doll" in crafted_toys and "Wooden train" in crafted_toys:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_values:
    print(f"Magic left: {', '.join([str(x) for x in magic_values])}")

sorted_toys = sorted(list(set(crafted_toys)))
for i in sorted_toys:
    print(f"{i}: {crafted_toys.count(i)}")

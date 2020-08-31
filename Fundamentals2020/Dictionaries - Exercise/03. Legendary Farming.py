key_materials = {}
junk = {}
magic_item = False

while not magic_item:
    if magic_item:
        break
    materials = input().split(" ")
    for i in range(0, len(materials), 2):
        key = materials[i + 1].lower()
        value = int(materials[i])
        if key == "shards" or key == "fragments" or key == "motes":
            if key not in key_materials:
                key_materials[key] = 0
            key_materials[key] += value
            for (key, value) in key_materials.items():
                if value >= 250:
                    if key == "shards":
                        print("Shadowmourne obtained!")
                    elif key == "fragments":
                        print("Valanyr obtained!")
                    elif key == "motes":
                        print("Dragonwrath obtained!")
                    key_materials[key] = value - 250
                    if "shards" not in key_materials:
                        key = "shards"
                        key_materials[key] = 0
                    if "fragments" not in key_materials:
                        key = "fragments"
                        key_materials[key] = 0
                    if "motes" not in key_materials:
                        key = "motes"
                        key_materials[key] = 0
                    magic_item = True
                    break
            if magic_item:
                break
        else:
            if key not in junk:
                junk[key] = 0
            junk[key] += value

sorted_key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))

for (key, value) in sorted_key_materials.items():
    print(f"{key}: {value}")
for (key, value) in sorted(junk.items()):
    print(f"{key}: {value}")

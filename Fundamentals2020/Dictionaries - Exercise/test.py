n = int(input())
register = {}

for i in range(n):
    line = input().split("<->")
    plant = line[0]
    rarity = int(line[1])
    register[plant] = [rarity]

while True:
    cmd = input()
    if "Exhibition" in cmd:
        break
    if "Rate" in cmd:
        cmd = cmd[6:].split(" - ")
        plant = cmd[0]
        rating = int(cmd[1])
        register[plant].append(rating)
    elif "Update" in cmd:
        cmd = cmd[8:].split(" - ")
        plant = cmd[0]
        new_rarity = int(cmd[1])
        register[plant][0] = new_rarity
    elif "Reset" in cmd:
        plant = cmd[7:]
        register[plant][1] = 0
    else:
        print("error")
for plant in register:
    av_rating = 0
    number_ratings = len(register[plant]) - 1
    for i in range(1, number_ratings + 1):
        av_rating += register[plant][i]
    av_rating /= number_ratings
    register[plant] = [register[plant][0], av_rating]

sorted_dict = dict(sorted(register.items(), key=lambda el: (-int(el[1][0]), -el[1][1])))

print("Plants for the exhibition:")
for plant in sorted_dict:
    rating = sorted_dict[plant][1]
    print(f"- {plant}; Rarity: {sorted_dict[plant][0]}; Rating: {rating:.2f}")

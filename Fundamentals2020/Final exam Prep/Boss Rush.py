n = int(input())

for i in range(n):
    valid = False
    boss = ""
    title = ""
    line = input().split(":")
    if len(line) == 2:
        bossp = line[0]
        titlep = line[1]
        bossS = bossp.split("|")
        titleS = titlep.split("#")
        if len(bossS) == 3 and len(titleS) == 3:
            boss = bossS[1]
            title = titleS[1]
            checktitle = title.split(" ")
            if len(checktitle) == 2 and checktitle[0].isalpha() and checktitle[1].isalpha():
                if len(boss) >= 4:
                    if boss.isupper():
                        valid = True

    if valid:
        print(f"{boss}, The {title}")
        print(f">> Strength: {len(boss)}")
        print(f">> Armour: {len(title)}")
    else:
        print("Access denied!")

n = int(input())

for i in range(n):
    valid = False
    line3 = ""
    line1 = input().split(">")
    line2 = line1[1].split("<")
    if len(line1) == 2 and len(line2) == 2:
        if line1[0] == line2[1] and line1[0] != "" and line2[1] != "" and len(line1[0]) >= 1 and len(line2[1]) >= 1:
            line3 = line2[0].split("|")
            if len(line3) == 4:
                if len(line3[0]) == 3 and len(line3[1]) == 3 and len(line3[2]) == 3 and len(line3[3]) == 3:
                    if line3[0].isdigit():
                        if line3[1].isalpha() and line3[1].islower():
                            if line3[2].isalpha() and line3[2].isupper():
                                if "<" not in line3[3]:
                                    if ">" not in line3[3]:
                                        valid = True
    if valid:
        password = line3[0] + line3[1] + line3[2] + line3[3]
        print(f"Password: {password}")
    else:
        print("Try another password!")

with open("./text.txt", "r") as text:
    for idx, line in enumerate(text):
        if idx % 2 == 0:
            for element in "-,.!?":
                line = line.replace(element, "@")
            words = reversed(line.split())
            print(" ".join(words))

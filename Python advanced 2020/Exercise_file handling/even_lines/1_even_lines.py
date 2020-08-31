# No input files creation is needed.
# The program will create all necessary files after initial run and entering input values.


with open("file.txt", "w") as file:
    text = input("Please enter the text"
                 " and after the last "
                 "line press Enter:\n")
    while text != "":
        file.write(text + "\n")
        text = input()

with open("file.txt", "r") as file:
    for i, line in enumerate(file):
        if i % 2 == 0:
            for el in "-,.!?":
                line = line.replace(el, "@")
            words = reversed(line.split())
            print(" ".join(words))

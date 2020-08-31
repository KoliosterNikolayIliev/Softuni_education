import os

def create(filename):
    with open(filename, "w") as file:
        file.write("")


def add(filename, content):
    with open(filename, "a") as file:
        file.write(content)
        file.write("\n")


def replace(filename, srch_str, repl_str):
    if os.path.exists(filename):
        text = ""
        with open(filename, "r") as file:
            text = file.read()
        text = text.replace(srch_str, repl_str)
        with open(filename, "w") as file:
            file.write(text)
    else:
        print("An error occurred")


def delete(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("An error occurred")

cmd = input()

while "End" not in cmd:

    tokens = cmd.split("-")
    if tokens[0] == "Create":
        create(tokens[1])

    elif tokens[0] == "Add":
        add(tokens[1],tokens[2])

    elif tokens[0] == "Replace":
        replace(tokens[1],tokens[2], tokens[3])

    elif tokens[0] == "Delete":
        delete(tokens[1])

    cmd = input()
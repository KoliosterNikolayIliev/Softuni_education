import os

while True:
    cmd_input = input()
    if cmd_input == "End":
        break
    cmd_input = cmd_input.split("-")
    command = cmd_input[0]
    file_name = cmd_input[1]
    if command == "Create":
        with open(file_name, "w") as file:
            continue
    elif command == "Add":
        content = cmd_input[2]
        with open(file_name, "a") as file:
            file.write(content + "\n")
    elif command == "Replace":
        old_string = cmd_input[2]
        new_string = cmd_input[3]
        if os.path.exists(file_name):
            text = ""
            with open(file_name, "r") as file:
                for line in file_name:
                    text += file.readline()
            if old_string in text:
                text = text.replace(old_string, new_string)
            with open(file_name, "w") as file:
                file.write(text)
        else:
            print("An error occurred")
    elif command == "Delete":
        try:
            os.remove("file.txt")
        except FileNotFoundError:
            print("An error occurred")

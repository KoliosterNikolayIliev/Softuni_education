import os

# Scroll further for code without functions


def create_file(file_name):
    with open(file_name, "w") as file:
        return file


def append_text_to_file(file_name, content):
    with open(file_name, "a") as file:
        return file.write(f"{content}\r")


def replace_string_in_file(file_name, old_string, new_string):
    try:
        with open(file_name, "r") as read_file:
            text = read_file.read()
            text = text.replace(old_string, new_string)
            with open(file_name, "w") as write_file:
                return write_file.write(text)
    except FileNotFoundError:
        return print("An error occurred")


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        return print("An error occurred")


while True:
    command = input().split("-")
    if command[0] == "End":
        break

    action = command[0]
    if action == "Create":
        create_file(command[1])

    elif action == "Add":
        append_text_to_file(command[1], command[2])

    elif action == "Replace":
        replace_string_in_file(command[1], command[2], command[3])

    elif action == "Delete":
        delete_file(command[1])


# Code without functions down below (use Ctrl + /)

# while True:
#     command = input().split("-")
#     if command[0] == "End":
#         break
#
#     action = command[0]
#     if action == "Create":
#         file_name = command[1]
#         with open(file_name, "w") as file:
#             continue
#
#     elif action == "Add":
#         file_name = command[1]
#         content = command[2]
#         with open(file_name, "a") as a_file:
#             a_file.write(f"{content}\r")
#
#     elif action == "Replace":
#         file_name = command[1]
#         old_string = command[2]
#         new_string = command[3]
#         try:
#             with open(file_name, "r") as r_file:
#                 text = r_file.read()
#                 text = text.replace(old_string,new_string)
#                 with open(file_name, "w") as w_file:
#                     w_file.write(text)
#         except FileNotFoundError:
#             print("An error occurred")
#     elif action == "Delete":
#         file_name = command[1]
#         try:
#             os.remove(file_name)
#         except FileNotFoundError:
#             print("An error occurred")

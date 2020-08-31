import os

line = input()

while line != 'End':

    tokens = line.split('-')
    command = tokens[0]
    file_name = tokens[1]

    if command == 'Create':
        file = open(file_name, 'w')
        file.close()

    elif command == 'Add':
        content = tokens[2]
        with open(file_name, 'a') as file:
            file.write(content)
            file.write('\n')

    elif command == 'Replace':
        old_string = tokens[2]
        new_string = tokens[3]
        try:
            with open(file_name, 'r') as file:
                text = file.read()
                text = text.replace(old_string, new_string)
            with open(file_name, 'w') as file:
                file.write(text)
        except FileNotFoundError:
            print('An error occurred')

    elif command == 'Delete':
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print('An error occurred')

    line = input()

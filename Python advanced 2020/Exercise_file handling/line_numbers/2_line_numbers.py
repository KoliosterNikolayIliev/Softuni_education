# No input files creation is needed.
# The program will create all necessary files after initial run and entering input values.

import string

with open("input.txt", "w") as file:
    text = input("Please enter the text"
                 " and after the last "
                 "line press Enter:\n")
    while text != "":
        file.write(text + "\n")
        text = input()

with open("input.txt", "r") as file:
    line_counter = 1
    with open("output.txt", "w") as file_out:
        for line in file:
            letters_count = 0
            punct_counter = 0
            for el in line:
                if el in string.punctuation:
                    punct_counter += 1
                if el.isalpha():
                    letters_count += 1
            file_out.write(f"Line {line_counter}: {line.strip()} ({letters_count})({punct_counter})\n")
            line_counter += 1

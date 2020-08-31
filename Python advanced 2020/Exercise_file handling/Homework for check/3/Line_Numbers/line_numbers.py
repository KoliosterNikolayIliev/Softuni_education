import string

punctuation_symbols = string.punctuation

with open("line_numbers_input.txt", "w") as f:
    f.writelines(["-I was quick to judge him, but it wasn't his fault.\n",
                  "-Is this some kind of joke?! Is it?\n",
                  "-Quick, hide here. It is safer.\n"])

with open("line_numbers_output.txt", "w") as output_file:
    with(open("line_numbers_input.txt", "r")) as input_file:
        count = 1
        for idx, line in enumerate(input_file):
            line = line.strip("\n")
            letters = len([x for x in line if x.isalpha()])
            puncts = len([x for x in line if x in punctuation_symbols])
            output_file.write(f"Line {idx + 1}: {line} ({letters})({puncts})\n")

with open("even_lines.txt", "w") as file:
    file.writelines(["-I was quick to judge him, but it wasn't his fault.\n",
                     "-Is this some kind of joke?! Is it?\n",
                     "-Quick, hide here. It is safer.\n"])

with open("even_lines.txt", "r") as file:
    symbols = ["-", ",", ".", "!", "?"]
    for index, line in enumerate(file.readlines()):
        if index % 2 != 0:
            continue
        for sym in symbols:
            if sym in line:
                line = line.replace(sym, "@")
        print(' '.join(line.split()[::-1]))

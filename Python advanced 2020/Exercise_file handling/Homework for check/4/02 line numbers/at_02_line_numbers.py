result = ""
with open("./text.txt", "r") as text:
    for idx, line in enumerate(text):
        c_punct = 0
        punctuation = [chr(x) for x in (range(33, 48))] + \
                      [chr(x) for x in (range(58, 64))]

        c_lttrs = 0
        letters = [chr(x) for x in range(65, 91)] + \
                  [chr(x) for x in range(97, 123)]

        for char in line:
            if char in punctuation:
                c_punct += 1
            if char in letters:
                c_lttrs += 1

        result += f" Line {idx + 1}: {line[:-2]} ({c_punct})({c_lttrs})\n"

with open("output.txt", "w") as outp:
    outp.write(result)

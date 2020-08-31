elements = ["-", ",", ".", "!", "?", "'", '"', ";", ":", "/"]

with open('text.txt', 'r') as file:
    result = ''
    for (index, line) in enumerate(file):
        line_length = len([el for el in line if el.isalpha()])
        counter = 0
        for el in line:
            if el in elements:
                counter += 1
        # print(f'Line {index + 1}: {line[:-1]} ({line_length})({counter})')
        result += f'Line {index + 1}: {line[:-1]} ({line_length})({counter})\n'

with open('output.txt', 'w') as f:
    f.write(result)

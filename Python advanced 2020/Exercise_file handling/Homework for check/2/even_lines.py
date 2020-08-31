elements = ['-', ',', '.', '!', '?']

with open('text.txt', 'r') as file:
    for (index, line) in enumerate(file):
        if index % 2 == 0:
            for el in elements:
                line = line.replace(el, '@')
            reversed_words = reversed(line.split())
            print(' '.join(reversed_words))

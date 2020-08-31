ascii_char1 = int(input())
ascii_char2 = int(input())
for i in range(ascii_char1, ascii_char2 + 1):
    ascii_char = chr(i)
    print(f'{ascii_char}', end=' ')

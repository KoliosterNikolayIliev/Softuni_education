words = input().split()

for word in words:
    new_word = ''
    first_letter_ascii = [char for char in word if char.isdigit()]
    left_chars = [char for char in word if char.isalpha()]
    left_chars[0], left_chars[-1] = left_chars[-1], left_chars[0]
    first_letter_ascii = chr(int(''.join(first_letter_ascii)))
    new_word += first_letter_ascii
    new_word += ''.join(left_chars)
    print(new_word, end=' ')

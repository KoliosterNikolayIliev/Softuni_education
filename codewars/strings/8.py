def first_non_repeating_letter(string):
    lower_string = string.lower()
    res = ""
    for letter in lower_string:
        if lower_string.count(letter) == 1:
            res = string[lower_string.index(letter)]
            break
    return res


print(first_non_repeating_letter('stress'))

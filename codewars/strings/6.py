def duplicate_encode(word):
    result = ""
    word = word.lower()
    for char in word:
        counter = word.count(char)
        if counter > 1:
            result += ")"
        else:
            result += "("
    return result


word = "Success"
print(duplicate_encode(word))

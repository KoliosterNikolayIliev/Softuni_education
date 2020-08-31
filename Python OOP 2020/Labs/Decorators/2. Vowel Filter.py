def vowel_filter(function):
    def wrapper():
        vowels = [x for x in function() if x.lower() in "aeiou"]
        return vowels

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())

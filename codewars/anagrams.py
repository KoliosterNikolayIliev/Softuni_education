# def anagrams(word, words):
#     anagrams = []
#     counts = {}
#     for letter in word:
#         counts[letter] = word.count(letter)
#
#     for word in words:
#         count_current_word = {}
#         for letter in word:
#             count_current_word[letter] = word.count(letter)
#         if counts == count_current_word:
#             anagrams.append(word)
#
#     return anagrams

# def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]
#
# print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
# print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))


def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(7))

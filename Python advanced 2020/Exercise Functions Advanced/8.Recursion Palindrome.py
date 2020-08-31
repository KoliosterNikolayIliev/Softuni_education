def palindrome(word, idx):
    second_idx = len(word) - 1 - idx
    if idx == len(word) // 2:
        return f"{word} is a palindrome"
    if word[idx] == word[second_idx]:
        return palindrome(word, idx + 1)
    else:
        return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
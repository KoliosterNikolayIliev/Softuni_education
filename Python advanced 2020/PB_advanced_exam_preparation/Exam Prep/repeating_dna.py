def get_repeating_DNA(string):
    result = []
    ll = []
    for i in range(0, len(string) - 10):
        current = string[i:i + 10]
        if current in string[i + 1:] and current not in result:
            result.append(current)
    return result


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)
#
# test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
# result = get_repeating_DNA(test)
# print(result)

# test = "AAAAAAAAAAA"
# result = get_repeating_DNA(test)
# print(result)

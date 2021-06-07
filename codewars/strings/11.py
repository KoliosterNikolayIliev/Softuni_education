def generate_hashtag(s):
    if s == '':
        return 'false'
    s = s.split(' ')
    result = '#'
    for word in s:
        word = word.strip().capitalize()
        result += word
    if len(result) > 140:
        return 'false'
    return result


print(generate_hashtag(" Hello there thanks for trying my Kata"))  # "#HelloThereThanksForTryingMyKata"
print(generate_hashtag("    Hello     World   "))  # "#HelloWorld"
print(generate_hashtag(""))  # false

# def generate_hashtag(s):
#     ans = '#'+ str(s.title().replace(' ',''))
#     return s and not len(ans)>140 and ans or False
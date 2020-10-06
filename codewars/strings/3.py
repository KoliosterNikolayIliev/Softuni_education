def find_short(s:str):
    return min([len(x) for x in s.split()])



words = "bitcoin take over the world maybe who knows perhaps"
print(find_short(words))
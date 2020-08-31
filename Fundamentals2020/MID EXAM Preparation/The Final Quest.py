words = input().split(" ")

while True:
    command = input().split(" ")
    cmd = command[0]
    if cmd == "Delete":
        index = int(command[1])+1
        if 0 <= index < len(words):
            del words[index]

    elif cmd == "Swap":
        word1 = command[1]
        word2 = command[2]
        if word1 in words and word2 in words:
            a, b = words.index(word1), words.index(word2)
            words[a], words[b] = words[b], words[a]

    elif cmd == "Put":
        word = command[1]
        index = int(command[2])-1
        if 0 <= index <= len(words):
            words.insert(index, word)
        # elif (index-1) == len(words):
        #     words.append(word)

    elif cmd == "Sort":
        words.sort(reverse=True)
    elif cmd == "Replace":
        word1 = command[1]
        word2 = command[2]
        if word2 in words:
            words[words.index(word2)] = word1
    elif cmd == "Stop":
        break

print(" ".join(words))

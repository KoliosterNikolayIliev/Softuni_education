text = input()
encrypted = []
for i in text:
    encrypted.append(chr(ord(i) + 3))
print("".join(encrypted))

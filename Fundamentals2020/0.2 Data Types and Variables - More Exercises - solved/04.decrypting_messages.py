key = int(input())
numberOfInputLines = int(input())
decryptedMsg = ""
for i in range(1,numberOfInputLines+1):
    char = input()
    decryptedMsg += (chr(ord(char) + key))
print(decryptedMsg)
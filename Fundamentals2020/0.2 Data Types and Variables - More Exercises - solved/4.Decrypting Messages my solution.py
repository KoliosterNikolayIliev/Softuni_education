key = int(input())
n = int(input())
decrypted = ""
for i in range(1, n + 1):
    char = input()
    decryption1 = ord(char)
    decryption2 = decryption1 + key
    decryption3 = chr(decryption2)
    decrypted += decryption3
print(decrypted)

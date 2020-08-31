lines = int(input())
sum = 0
for i in range(lines):
    char = input()
    ascii_num = ord(char)
    sum = sum + ascii_num
print(f'The sum equals: {sum}')

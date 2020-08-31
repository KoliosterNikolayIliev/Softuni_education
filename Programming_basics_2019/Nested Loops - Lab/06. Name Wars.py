name = input()
max_sum = 0
winner_name = ''
while name != 'STOP':
    current_sum = 0
    for char in name:
        ascii_value = ord(char)
        current_sum += ascii_value
    if current_sum > max_sum:
        max_sum = current_sum
        winner_name = name
    name = input()
print(f'Winner is {winner_name} - {max_sum}!')

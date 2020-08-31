command = input()
notes = []
while command != 'End':
    tokens = command.split('-')
    priority = int(tokens[0])
    note = tokens[1]
    notes[priority - 1] = note
    command = input()
result = []
for element in notes:
    if element != 0:
        result.append(element)
print(result)

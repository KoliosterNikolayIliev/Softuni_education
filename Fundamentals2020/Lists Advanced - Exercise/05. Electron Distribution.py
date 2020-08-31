electrons = int(input())

shells = []

shell_index = 1
while electrons > 0:
    max_electrons = 2 * shell_index ** 2
    if max_electrons > electrons:
        max_electrons=electrons
    shells.append(max_electrons)
    electrons -= max_electrons
    shell_index += 1
print(shells)

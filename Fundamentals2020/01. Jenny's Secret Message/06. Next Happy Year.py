year = input()
current_year = year
found_year = True

while True:
    current_year = int(current_year) + 1
    found_year = True
    for first_index in range(len(year)):
        for second_index in range(first_index + 1, len(year)):
            first_digit = str(current_year)[first_index]
            second_digit = str(current_year)[second_index]
            if first_digit == second_digit:
                found_year = False
                break
    if found_year:
        print(current_year)
        break

year = input()

#while True:
#    year = str(int(year) + 1)
#    if len(set(year)) == len(year):
#        print(year)
#        break

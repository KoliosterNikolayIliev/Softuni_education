first_name = input()
last_name = input()
age = int(input())
town = input()

#'You are {first_name} {last name}, a {age} - years old person from {town}

print('You are ' + first_name + '' + last_name + ', a' + str(age) + '- years old')
print('.................')
print(f'You are {first_name} {last_name}, a {age+5}-years old person from {town}')
command = input()
coffee_counter = 0
while command != "END":
    if command.upper() == command:
        if command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
            coffee_counter += 2
    if command.lower() == command:
        if command == "coding" or command == "dog" or command == "cat" or command == "movie":
            coffee_counter += 1
    command = input()
if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)
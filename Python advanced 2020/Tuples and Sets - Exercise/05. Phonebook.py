contact_list = dict()
n = 0
while True:
    contacts = input()
    if contacts.isdigit():
        n = int(contacts)
        break
    contacts = contacts.split("-")
    name = contacts[0]
    number = contacts[1]
    contact_list[name] = number

for i in range(n):
    searched_name = input()
    if searched_name in contact_list:
        print(f"{searched_name} -> {contact_list[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")

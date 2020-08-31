import re

n = int(input())

pattern = r"U\$([A-Z][a-z]{2,})U\$P@\$([A-Za-z]{5,}\d+)P@\$"
username_pattern = r"U\$([A-Z][a-z]{2,})U\$"
password_pattern = r"P@\$([A-Za-z]{5,}\d+)P@\$"
counter = 0
for i in range(n):
    registration = input()
    match = re.match(pattern, registration)

    if match is None:
        print("Invalid username or password")
        continue
    Username = match[1]
    Password = match[2]
    counter += 1
    print("Registration was successful")

    print(f"Username: {Username}, Password: {Password}")

print(f"Successful registrations: {counter}")
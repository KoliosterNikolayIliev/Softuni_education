lost_fights = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
expenses = 0
counter=0
for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        expenses += helmet
    if i % 3 == 0:
        expenses += sword
        if i % 2 == 0:
            expenses += shield
            counter+=1
            if counter % 2 == 0:
                expenses += armor
print(f"Gladiator expenses: {expenses:.2f} aureus")

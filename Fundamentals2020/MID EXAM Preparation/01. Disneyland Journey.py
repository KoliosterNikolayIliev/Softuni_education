cost = float(input())
months = int(input())
saved_money = 0
savings = 0
for month in range(1, months + 1):
    saved_money = 0.25 * cost

    if month % 2 != 0 and month != 1:
        savings -= 0.16 * savings
    if month % 4 == 0:
        savings += savings * 0.25
    savings += saved_money

if savings >= cost:
    print(f"Bravo! You can go to Disneyland and you will have {(savings - cost):.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {(cost - savings):.2f}lv. more.")

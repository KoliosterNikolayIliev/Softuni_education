locations=int(input())
#real_total=0
#real_average=0
#average_gold_diged=0
for i in range (locations):
    average_gold_diged=float(input())
    days_for_dig=int(input())
    real_total = 0
    real_average = 0
    for n in range(days_for_dig):
        day_gold_diged=float(input())
        real_total+=day_gold_diged
        real_average=real_total/days_for_dig
    if real_average>=average_gold_diged:
        print(f"Good job! Average gold per day: {real_average:.2f}.")
    else:
        print(f"You need {(average_gold_diged-real_average):.2f} gold.")

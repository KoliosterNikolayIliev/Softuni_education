budget = float(input())
category = input()
number_of_people = int(input())

vip_ticket = 499.99
normal_ticket = 249.99


if category=="VIP":
    if 1<= number_of_people<=4:
        total=number_of_people*vip_ticket
        ticket_money=budget-0.75*budget
        money_left=ticket_money - total
        if money_left>0:
            print(f"Yes! You have {(money_left):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(abs(money_left)):.2f} leva.")

    elif 5<= number_of_people<=9:
        total=number_of_people*vip_ticket
        ticket_money=budget-0.60*budget
        money_left=ticket_money - total
        if money_left>0:
            print(f"Yes! You have {(money_left):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(abs(money_left)):.2f} leva.")
    elif 10<= number_of_people<=24:
        total=number_of_people*vip_ticket
        ticket_money=budget-0.50*budget
        money_left=ticket_money - total
        if money_left>0:
            print(f"Yes! You have {(money_left):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(abs(money_left)):.2f} leva.")
    elif 25<= number_of_people<=49:
        total=number_of_people*vip_ticket
        ticket_money=budget-0.40*budget
        money_left=ticket_money - total
        if money_left>0:
            print(f"Yes! You have {(money_left):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(abs(money_left)):.2f} leva.")
    elif number_of_people>=50:
        total=number_of_people*vip_ticket
        ticket_money=budget-0.25*budget
        money_left=ticket_money - total
        if money_left>0:
            print(f"Yes! You have {(money_left):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(abs(money_left)):.2f} leva.")

elif category=="Normal":
    if 1<= number_of_people<=4:
        total=number_of_people*normal_ticket
        ticket_money=budget-0.75*budget
        money_left=ticket_money - total
        if money_left>0:
            print(f"Yes! You have {(money_left):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(abs(money_left)):.2f} leva.")
    elif 5<= number_of_people<=9:
        total=number_of_people*normal_ticket
        ticket_money=budget-0.60*budget
        money_left=ticket_money - total
        if money_left>0:
            print(f"Yes! You have {(money_left):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(abs(money_left)):.2f} leva.")
    elif 10>= number_of_people<=24:
        total=number_of_people*normal_ticket
        ticket_money=budget-0.50*budget
        money_left=ticket_money - total
        if money_left>0:
            print(f"Yes! You have {(money_left):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(abs(money_left)):.2f} leva.")
    elif 25>= number_of_people<=49:
        total=number_of_people*normal_ticket
        ticket_money=budget-0.40*budget
        money_left=ticket_money - total
        if money_left>0:
            print(f"Yes! You have {(money_left):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(abs(money_left)):.2f} leva.")
    elif number_of_people>=50:
        total=number_of_people*normal_ticket
        ticket_money=budget-0.25*budget
        money_left=ticket_money - total
        if money_left>0:
            print(f"Yes! You have {(money_left):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(abs(money_left)):.2f} leva.")


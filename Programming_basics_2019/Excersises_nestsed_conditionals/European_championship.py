budget = float(input())
category = input()
number_of_people = int(input())

vip_ticket = 499.99
normal_ticket = 249.99
total_ticket_price_VIP = number_of_people * vip_ticket
total_ticket_price_Normal = number_of_people * normal_ticket

if 1 <= number_of_people and number_of_people<= 4:
    money_left = budget - (0.75 * budget)

    if category == 'VIP':
        if money_left >= total_ticket_price_VIP:
            ticket_money_left = money_left - total_ticket_price_VIP
            print(f"Yes! You have {(ticket_money_left):.2f} leva left.")
        else:
            ticket_money_left = money_left - total_ticket_price_VIP
            print(f"Not enough money! You need {(abs(ticket_money_left)):.2f} leva.")

    elif category == 'Normal' and money_left >= total_ticket_price_Normal:
        if money_left >= total_ticket_price_Normal:
            ticket_money_left = money_left - total_ticket_price_Normal
            print(f"Yes! You have {(ticket_money_left):.2f} leva left.")
        else:
            ticket_money_left = money_left - total_ticket_price_Normal
            print(f"Not enough money! You need {(abs(ticket_money_left)):.2f} leva.")

if 5 <= number_of_people and number_of_people<= 9:
    money_left = budget - (0.6 * budget)

    if category == 'VIP':
        if money_left >= total_ticket_price_VIP:
            ticket_money_left = money_left - total_ticket_price_VIP
            print(f"Yes! You have {(ticket_money_left):.2f} leva left.")
        else:
            ticket_money_left = money_left - total_ticket_price_VIP
            print(f"Not enough money! You need {(abs(ticket_money_left)):.2f} leva.")

    elif category == 'Normal' and money_left >= total_ticket_price_Normal:
        if money_left >= total_ticket_price_Normal:
            ticket_money_left = money_left - total_ticket_price_Normal
            print(f"Yes! You have {(ticket_money_left):.2f} leva left.")
        else:
            ticket_money_left = money_left - total_ticket_price_Normal
            print(f"Not enough money! You need {(abs(ticket_money_left)):.2f} leva.")

if 10 <= number_of_people and number_of_people<= 24:
    money_left = budget - (0.50 * budget)

    if category == 'VIP':
        if money_left >= total_ticket_price_VIP:
            ticket_money_left = money_left - total_ticket_price_VIP
            print(f"Yes! You have {(ticket_money_left):.2f} leva left.")
        else:
            ticket_money_left = money_left - total_ticket_price_VIP
            print(f"Not enough money! You need {(abs(ticket_money_left)):.2f} leva.")

    elif category == 'Normal' and money_left >= total_ticket_price_Normal:
        if money_left >= total_ticket_price_Normal:
            ticket_money_left = money_left - total_ticket_price_Normal
            print(f"Yes! You have {(ticket_money_left):.2f} leva left.")
        else:
            ticket_money_left = money_left - total_ticket_price_Normal
            print(f"Not enough money! You need {(abs(ticket_money_left)):.2f} leva.")

if 25 <= number_of_people and number_of_people<= 49:
    money_left = budget - (0.40 * budget)

    if category == 'VIP':
        if money_left >= total_ticket_price_VIP:
            ticket_money_left = money_left - total_ticket_price_VIP
            print(f"Yes! You have {(ticket_money_left):.2f} leva left.")
        else:
            ticket_money_left = money_left - total_ticket_price_VIP
            print(f"Not enough money! You need {(abs(ticket_money_left)):.2f} leva.")

    elif category == 'Normal' and money_left >= total_ticket_price_Normal:
        if money_left >= total_ticket_price_Normal:
            ticket_money_left = money_left - total_ticket_price_Normal
            print(f"Yes! You have {(ticket_money_left):.2f} leva left.")
        else:
            ticket_money_left = money_left - total_ticket_price_Normal
            print(f"Not enough money! You need {(abs(ticket_money_left)):.2f} leva.")

if number_of_people >= 50:
    money_left = budget - (0.25 * budget)

    if category == 'VIP':
        if money_left >= total_ticket_price_VIP:
            ticket_money_left = money_left - total_ticket_price_VIP
            print(f"Yes! You have {(ticket_money_left):.2f} leva left.")
        else:
            ticket_money_left = money_left - total_ticket_price_VIP
            print(f"Not enough money! You need {(abs(ticket_money_left)):.2f} leva.")

    elif category == 'Normal' and money_left >= total_ticket_price_Normal:
        if money_left >= total_ticket_price_Normal:
            ticket_money_left = money_left - total_ticket_price_Normal
            print(f"Yes! You have {(ticket_money_left):.2f} leva left.")
        else:
            ticket_money_left = money_left - total_ticket_price_Normal
            print(f"Not enough money! You need {(abs(ticket_money_left)):.2f} leva.")

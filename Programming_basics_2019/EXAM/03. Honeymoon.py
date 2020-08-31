budget=float(input())
city=input()
nights_count=int(input())
sum=0
if city=='Cairo':
    night_price=250
    total_nights_price=nights_count*(night_price*2)
    flight_price=600
    sum=total_nights_price+flight_price
    if 1<=nights_count<=4:
        sum*=0.97
    elif 5<=nights_count<=9:
        sum*=0.95
    elif 10 <= nights_count <= 24:
        sum *= 0.90
    elif 25 <= nights_count <= 49:
        sum *= 0.83
    elif 50 <= nights_count:
        sum *= 0.70

elif city=='Paris':
    night_price=150
    total_nights_price=nights_count*(night_price*2)
    flight_price=350
    sum=total_nights_price+flight_price

    if 5<=nights_count<=9:
        sum*=0.93
    elif 10 <= nights_count <= 24:
        sum *= 0.88
    elif 25 <= nights_count <= 49:
        sum *= 0.78
    elif 50 <= nights_count:
        sum *= 0.70

elif city=='New York':
    night_price=300
    total_nights_price=nights_count*(night_price*2)
    flight_price=650
    sum=total_nights_price+flight_price
    if 1<=nights_count<=4:
        sum*=0.97
    elif 5<=nights_count<=9:
        sum*=0.95
    elif 10 <= nights_count <= 24:
        sum *= 0.88
    elif 25 <= nights_count <= 49:
        sum *= 0.81
    elif 50 <= nights_count:
        sum *= 0.70

elif city=='Lima':
    night_price=400
    total_nights_price=nights_count*(night_price*2)
    flight_price=850
    sum=total_nights_price+flight_price

    if 25 <= nights_count <= 49:
        sum *= 0.81
    elif 50 <= nights_count:
        sum *= 0.70

elif city=='Tokyo':
    night_price=350
    total_nights_price=nights_count*(night_price*2)
    flight_price=700
    sum=total_nights_price+flight_price

    if 10 <= nights_count <= 24:
        sum *= 0.88
    elif 25 <= nights_count <= 49:
        sum *= 0.83
    elif 50 <= nights_count:
        sum *= 0.70
if budget >= sum:
    print(f"Yes! You have {(budget-sum):.2f} leva left.")
else:
    print(f"Not enough money! You need {(sum-budget):.2f} leva.")


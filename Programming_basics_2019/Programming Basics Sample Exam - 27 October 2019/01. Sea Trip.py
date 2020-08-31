food_money = float(input())
souvenirs_money = float(input())
hotel_money = float(input())
fuel_money = 54.39

expences_without_hotel = (food_money + souvenirs_money) * 3

hotel_day_1_money = hotel_money * 0.9
hotel_day_2_money = hotel_money * 0.85
hotel_day_3_money = hotel_money * 0.8

total_sum = fuel_money + expences_without_hotel + hotel_day_1_money + hotel_day_2_money + hotel_day_3_money
print(f'Money needed: {total_sum:.2f}')

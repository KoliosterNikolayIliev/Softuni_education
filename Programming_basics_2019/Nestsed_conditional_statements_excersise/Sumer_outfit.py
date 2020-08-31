temp_deg = int(input())
time_of_the_day = input()
outfit = ''
shoes = ''

if time_of_the_day == 'Morning':
    if 10 <= temp_deg <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < temp_deg <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif temp_deg >= 25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'

elif time_of_the_day == 'Afternoon':
    if 10 <= temp_deg <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < temp_deg <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif temp_deg >= 25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'

elif time_of_the_day == 'Evening':
    if 10 <= temp_deg <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < temp_deg <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif temp_deg >= 25:
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {temp_deg} degrees, get your {outfit} and {shoes}.")

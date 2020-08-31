month = input()
nights = int(input())

studio = 0
apartment = 0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if nights <= 7:
        studio = studio * nights
        apartment = apartment * nights
    elif 7 < nights < 14:
        studio = (studio * nights) * 0.95
        apartment = apartment * nights
    elif nights > 14:
        studio = (studio * nights) * 0.7
        apartment = (apartment * nights) * 0.9
    print(f'Apartment: {apartment:.2f} lv.')
    print(f'Studio: {studio:.2f} lv.')

elif month == 'June' or month == 'September':
    studio = 75.2
    apartment = 68.7

    if nights <= 14:
        studio = studio * nights
        apartment = apartment * nights
        print(f'Apartment: {apartment:.2f} lv.')
        print(f'Studio: {studio:.2f} lv.')
    elif nights > 14:
        studio = (studio * nights) * 0.8
        apartment = (apartment * nights) * 0.9

        print(f'Apartment: {apartment:.2f} lv.')
        print(f'Studio: {studio:.2f} lv.')


elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77

    if nights > 14:
        apartment = (apartment * nights) * 0.9
        studio = studio * nights
        print(f'Apartment: {apartment:.2f} lv.')
        print(f'Studio: {studio:.2f} lv.')

    elif nights <= 14:
        apartment = apartment * nights
        studio = studio * nights
        print(f'Apartment: {apartment:.2f} lv.')
        print(f'Studio: {studio:.2f} lv.')

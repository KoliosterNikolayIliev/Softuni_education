days = int(input())
room_type = input()
evaluation = input()

nights = days - 1
room_for_one_person = 18
apartment = 25
president_apartment = 35

final_price = 0

if days < 10:
    if room_type == 'room for one person':
        final_price = room_for_one_person * nights
        if evaluation == 'positive':
            final_price = final_price + (final_price * 0.25)
        elif evaluation == 'negative':
            final_price = final_price - (final_price * 0.1)
        print(f'{final_price:.2f}')

    elif room_type == 'apartment':
        final_price = apartment * nights - ((apartment * nights) * 0.3)
        if evaluation == 'positive':
            final_price = final_price + (final_price * 0.25)
        elif evaluation == 'negative':
            final_price = final_price - (final_price * 0.1)
        print(f'{final_price:.2f}')

    elif room_type == 'president apartment':
        final_price = president_apartment * nights - ((president_apartment * nights) * 0.1)
        if evaluation == 'positive':
            final_price = final_price + (final_price * 0.25)
        elif evaluation == 'negative':
            final_price = final_price - (final_price * 0.1)
        print(f'{final_price:.2f}')

elif 10 <= days <= 15:
    if room_type == 'room for one person':
        final_price = room_for_one_person * nights
        if evaluation == 'positive':
            final_price = final_price + (final_price * 0.25)
        elif evaluation == 'negative':
            final_price = final_price - (final_price * 0.1)
        print(f'{final_price:.2f}')

    elif room_type == 'apartment':
        final_price = apartment * nights - ((apartment * nights) * 0.35)
        if evaluation == 'positive':
            final_price = final_price + (final_price * 0.25)
        elif evaluation == 'negative':
            final_price = final_price - (final_price * 0.1)
        print(f'{final_price:.2f}')

    elif room_type == 'president apartment':
        final_price = president_apartment * nights - ((president_apartment * nights) * 0.15)
        if evaluation == 'positive':
            final_price = final_price + (final_price * 0.25)
        elif evaluation == 'negative':
            final_price = final_price - (final_price * 0.1)
        print(f'{final_price:.2f}')

elif days > 15:
    if room_type == 'room for one_person':
        final_price = room_for_one_person * nights
        if evaluation == 'positive':
            final_price = final_price + (final_price * 0.25)
        elif evaluation == 'negative':
            final_price = final_price - (final_price * 0.1)
        print(f'{final_price:.2f}')

    elif room_type == 'apartment':
        final_price = apartment * nights - ((apartment * nights) * 0.5)
        if evaluation == 'positive':
            final_price = final_price + (final_price * 0.25)
        elif evaluation == 'negative':
            final_price = final_price - (final_price * 0.1)
        print(f'{final_price:.2f}')

    elif room_type == 'president apartment':
        final_price = president_apartment * nights - ((president_apartment * nights) * 0.2)
        if evaluation == 'positive':
            final_price = final_price + (final_price * 0.25)
        elif evaluation == 'negative':
            final_price = final_price - (final_price * 0.1)
        print(f'{final_price:.2f}')

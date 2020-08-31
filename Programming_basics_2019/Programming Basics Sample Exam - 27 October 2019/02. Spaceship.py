import math

ship_w = float(input())
ship_l = float(input())
ship_h = float(input())
av_spacemen_h = float(input())

ship_vol = ship_h * ship_l * ship_w
room_volume = (av_spacemen_h + 0.4) * 2 * 2
spaceman_count = math.floor(ship_vol / room_volume)

if 10 >= spaceman_count >= 3:
    print(f'The spacecraft holds {spaceman_count} astronauts.')
elif spaceman_count < 3:
    print("The spacecraft is too small.")
else:
    print("The spacecraft is too big.")

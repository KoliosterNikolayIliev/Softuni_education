lenght=int(input()) #cm
width=int(input()) #cm
height=int(input()) #cm
fill_perc=float(input()) #%
total_volume = lenght*width*height #cm3
total_volume_l= total_volume*0.001
percent_dig = fill_perc*0.01
water_volume=total_volume_l-(total_volume_l*percent_dig)
print(f'{water_volume:.3f}')


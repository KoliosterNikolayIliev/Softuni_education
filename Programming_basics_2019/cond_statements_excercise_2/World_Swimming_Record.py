reccord_s = float(input())
distance_m = float(input())
time_s_m = float(input())
import math

ivan_time = distance_m * time_s_m
slowdown=distance_m/15
slowdown=math.floor(slowdown)
ivan_add_time = (slowdown) * 12.5
#ivan_add_time = math.ceil(ivan_add_time)
ivan_cor_time = ivan_time + ivan_add_time
#ivan_cor_time = math.floor(ivan_cor_time)

not_enough_time = ivan_cor_time - reccord_s
#not_enough_time = math.floor(not_enough_time)

if ivan_cor_time < reccord_s:
    print(f'Yes, he succeeded! The new world record is {ivan_cor_time:.2f} seconds.')

else:
    print(f'No, he failed! He was {not_enough_time:.2f} seconds slower.')

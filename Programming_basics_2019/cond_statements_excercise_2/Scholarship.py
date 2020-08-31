income = float(input())
avg_mark = float(input())
min_sallary = float(input())

import math

social_scolarship = min_sallary * 0.35
excellent_scolarship = avg_mark * 25

if avg_mark >= 4.5 and avg_mark < 5.5 and income < min_sallary:
    result1 = math.floor(social_scolarship)
    print(f'You get a Social scholarship {result1} BGN')

elif avg_mark >= 5.5: # and income > min_sallary:
    result2 = math.floor(excellent_scolarship)
    print(f'You get a scholarship for excellent results {result2} BGN')

elif avg_mark >= 5.5 and income < min_sallary and social_scolarship > excellent_scolarship:
    result3 = math.floor(social_scolarship)
    print(f'You get a Social scholarship {result3} BGN')

elif avg_mark >= 5.5 and income < min_sallary and social_scolarship < excellent_scolarship:
    result4 = math.floor(excellent_scolarship)
    print(f'You get a scholarship for excellent results {result4} BGN')

elif avg_mark >= 5.5 and income < min_sallary and social_scolarship == excellent_scolarship:
    result5 = math.floor(excellent_scolarship)
    print(f'You get a scholarship for excellent results {result5} BGN')

else:
    print('You cannot get a scholarship!')

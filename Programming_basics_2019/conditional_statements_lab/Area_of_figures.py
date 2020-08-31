figure=input('')
import math
from math import pi
if figure=='square':
    side=float(input())
    area=side**2
    print(f'{area:.3f}')
elif figure=='rectangle':
    a=float(input())
    b=float(input())
    area=a*b
    print(f'{area:.3f}')
elif figure == 'circle':
    r = float(input())
    area = pi*r**2
    print(f'{area:.3f}')
elif figure=='triangle':
    c=float(input())
    h=float(input())
    area=(c*h)/2
    print(f'{area:.3f}')

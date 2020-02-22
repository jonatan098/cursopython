import math
catop = float(input('digite o angulo do cateto oposto '))
catad = float(input('digite o angulo do cateto adjcente '))
hip = math.hypot(catop, catad)
print(f'a hipotenusa é = {hip:.2f}')
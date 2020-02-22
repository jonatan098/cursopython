import math
ang = float(input('digite o angulo desejado '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'o angulo {ang} tem seno de {sen:.2f}')
print(f'o angulo {ang} tem cosseno de {cos:.2f}')
print(f'o angulo {ang} tem tangente de {tan:.2f}')
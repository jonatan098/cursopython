dist = float(input('qual a distancia da sua viagem? '))
if dist <= 200:
    print(f'o preço da passagem e de R${(dist*0.50):.2f}')
else:
    print(f'o preço da passagem e de R${(dist*0.45):.2f}')
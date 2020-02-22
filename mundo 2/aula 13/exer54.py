#GRUPO DA MAIORIDADE
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    nasc = int(input(f'em que ano a {c}ª pessoa nasceu: '))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'das {c} pessoas {maior} são maiore(s)')
print(f'e {menor} são menore(s)')
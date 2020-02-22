from datetime import date
atual = date.today().year
nasc = int(input('em qual ano voce nasceu? '))
idade = 2019 - nasc
print(f'quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade < 18:
    print(f'ainda falta(m) {18 - idade} ano(s) para o alistamento.')
    print(f'seu alistamento sera em {nasc + 18}.')
elif idade == 18:
    print('voce tem que se alistar imediatamente.')
else:
    print(f'voce ja teveria ter feito o alistamento há {idade - 18} ano(s).')
    print(f'seu alistamento foi em {nasc + 18}.')

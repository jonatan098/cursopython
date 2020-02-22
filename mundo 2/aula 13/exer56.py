idadetot = 0
velho = 0
numbM = 0
for c in range(1,5):
    print(f'------- {c}ª PESSOA -------')
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]: ')).upper()
    idadetot += idade
    if idade > velho and sexo == 'M':
        nomev = nome
        velho = idade
    if sexo == 'F' and idade < 20:
        numbM += 1
print(f'a media de idade do grupo é de {idadetot/c}')
print(f'o homen mais velho se chama {nomev} é tem {velho} anos')
print(f'ao todo são {numbM} mulhere(s) menores de 20 anos')

#VARIOS NÚMEROS COM FLAG
cont = soma = 0
while True:
    n = int(input('digite um valor [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma = soma + n
print(f'a soma dos {cont} foi {soma}')
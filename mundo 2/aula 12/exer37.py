num = int(input('digite um numero inteiro: '))
print('''escolha um das bases de converção: 
[ 1 ] converter para binario
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
ops = int(input('sua opção: '))
if ops == 1:
    print(f'{num} convertido para binario e igual a {bin(num)[2:]}')
elif ops == 2:
    print(f'{num} convertido para octal e igual a {oct(num)[2:]}')
elif ops == 3:
    print(f'{num} convertido para hexadecimal e igual a {hex(num)[2:]}')
else:
    print('opção invalida. tente novamente')
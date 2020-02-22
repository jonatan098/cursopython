numb = int(input('digite um numero: '))
result = numb%2
if result == 0:
    print(f'{numb} e \033[0;34;0mPAR')
else:
    print(f'{numb} e \033[0;33;0mIMPAR')
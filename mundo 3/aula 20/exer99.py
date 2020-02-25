from time import sleep
def maior(*num):
    maiorn = 0
    print('analisando os valores passados...')
    for n in num:
        print(n, end=' ',flush=True)
        sleep(0.5)
        if n > maiorn:
            maiorn = n
    print(f'foram informados {len(num)} valores ao todo.')
    print(f'o maior valor informado foi {maiorn}')
    print('-='*30)
#main cod
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
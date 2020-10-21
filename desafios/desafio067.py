cont=0

while True:
    n=int(input('Digite um valor para saber a sua tabuada: '))
    if n < 0:
        break
    print('-'*20)
    for cont in range(1,11):
        print(f'{n} x {cont} = {n*cont}')
        cont+=1
    print('-'*20)
print('PROGRAMA ENCERRADO.')

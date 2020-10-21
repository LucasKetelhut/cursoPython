n=int(input('Digite um número para obter o seu fatorial: '))
cont=n
fatorial=1
print(f'{n}! → ',end='')
while cont > 0:
    print(f'{cont}',end='') 
    print(' x ' if cont > 1 else ' = ',end='')
    fatorial *= cont
    cont-=1
print(f'{fatorial}')

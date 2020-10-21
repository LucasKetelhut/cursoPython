n1=int(input('Digite o 1º número: '))
n2=int(input('Digite o 2º número: '))
n3=int(input('Digite o 3º número: '))
n4=int(input('Digite o 4º número: '))
tupla=(n1,n2,n3,n4)
print(f'Você digitou os números: {tupla}')

if 9 in tupla:
    print(f'O valor 9 apareceu {tupla.count(9)} vez(es)')
else:
    print('O valor 9 não apareceu nenhuma vez')
if 3 in tupla:
    print(f'O valor 3 foi digitado pela primeira vez na posição {tupla.index(3)+1}')
else:
    print('O valor 3 não foi digitado nenhuma vez')

print('Os valores pares digitados foram:',end = ' ')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
print('\n')        

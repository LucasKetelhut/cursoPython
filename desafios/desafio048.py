soma=0

for i in range(1,501):
    if (i%2) !=0:
        if (i%3) == 0:
            soma += i
print('A soma entre todos os números ímpares que são múltiplos de três',end=' ')
print(f'e que se encontram no intervalo de 1 até 500 é de {soma}')

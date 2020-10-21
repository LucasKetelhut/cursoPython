matriz=[[0,0,0],[0,0,0],[0,0,0]]
somapares=somaterceira=maior=0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna]=int(input(f'Digite um valor para [{linha},{coluna}]: '))
        if linha == 0 and coluna == 0:
            maior=matriz[linha][coluna]
        if matriz[linha][coluna] % 2 == 0:
            somapares += matriz[linha][coluna]
        if coluna == 2:
            somaterceira+=matriz[linha][coluna]
        if linha == 1:
            if matriz[linha][coluna]> maior:
                maior=matriz[linha][coluna]
print('-='*40)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end=' ')
    print()
print('-='*40)
print(f'A soma dos valores pares é {somapares}')
print(f'A soma dos valores da terceira coluna é {somaterceira}')
print(f'O maior valor da segunda linha é {maior}')
print()

digitados = soma = n = maior = menor = 0
opção=''

while opção != 'N':
    n=int(input('Digite um valor: '))  
    soma+=n
    digitados+=1
    if digitados == 1:
        maior = menor = n
    else:
        if n > maior:
            maior=n
        if n < menor:
            menor=n    
    opção=str(input('Quer continuar a digitar valores? [S/N]: ')).strip().upper()

print(f'\nVocê digitou {digitados} números.')
print(f'Dentre os números digitados, o maior foi {maior}',end=' ')
print(f'e o menor foi {menor}!')
print('Média entre os números digitados = {:.2f}\n'.format(soma/digitados))

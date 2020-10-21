homens=maior18=menos20=idade=0
sexo=opção=''

while True:
    print('-'*30)
    print('     CADASTRE UMA PESSOA!')
    print('-'*30)
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).strip().upper()
    while sexo != 'M' and sexo != 'F':
            sexo=str(input('Sexo [M/F]: ')).strip().upper()
    if sexo == 'M':
        homens+=1
    if sexo == 'F' and idade < 20:
        menos20+=1
    if idade > 18:
        maior18 +=1
    opção=str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while opção != 'S' and opção != 'N':
            opção=str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if opção == 'N':
        break
print('\n============ FIM DO PROGRAMA ============')
print(f'\nTemos {maior18} pessoa(s) com mais de 18 anos!')
print(f'Ao todo foram cadastrados {homens} homens.')
print(f'{menos20} mulheres tem menos de 20 anos!\n')

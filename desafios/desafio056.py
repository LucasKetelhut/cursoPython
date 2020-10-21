soma=0
media=0
maior=0
velho=''
mulher20=0

for i in range(1,5):
    print(f'----- {i}ª PESSOA -----')
    nome=str(input('Nome: ')).strip()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).strip().upper()
    if(i==1) and sexo == 'M':
        maior=idade
        velho=nome
    if sexo == 'M' and idade > maior:
        maior=idade
        velho=nome    
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    soma+=idade
media=soma/4
print('A média de idade do grupo é de {:.1f} anos.'.format(media))
print(f'O homem mais velho tem {maior} anos e se chama {velho}.')
print(f'Ao todo, são {mulher20} mulher(es) com menos de 20 anos.')

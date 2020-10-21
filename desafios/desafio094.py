galera=[]
pessoa={}
soma=media=0

while True:
    pessoa.clear()
    pessoa['Nome']=str(input('Nome: ')).strip()
    while True:
        pessoa['Sexo']=str(input('Sexo [M/F]: ')).strip().upper()
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade']=int(input('Idade: '))
    soma+=pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        opção=str(input('Quer continuar? [S/N]: ')).strip().upper()
        if opção in 'SN':
            break
        print('ERRO! Responda apenas com S ou N.')
    if opção in 'N':
        break
media=soma/len(galera)
print('-'*40)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'A média de idade é de {media:.2f} anos.')
print(f'As mulheres cadastradas foram: ',end='')
for pessoa in galera:
    if pessoa['Sexo'] == 'F':
        print(f'{pessoa["Nome"]} ',end='')
print()
print('Lista de pessoas que estão acima da média: ',end='')
for pessoa in galera:
    if pessoa['Idade'] >= media:
        print(f'{pessoa["Nome"]} ',end='')
print()
print('<< ENCERRADO >>')

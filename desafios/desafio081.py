lista=[]

while True:
    lista.append(int(input('Insira um valor: ')))
    opção=str(input('Quer continuar? [S/N]: ')).strip().upper()
    if opção in 'Nn':
        break
print(f'\nOs números digitados foram: {lista}')
if 5 in lista:
    print('Sim! O valor 5 está na lista!')
else:
    print('Não! O valor 5 não foi digitado e não está na lista.')
print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'A lista ordenada de forma decrescente fica assim: {lista}\n')

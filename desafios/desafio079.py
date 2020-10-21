lista=[]
n=0 

while True:
    n=int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso...')    
    opção=str(input('Quer continuar? [S/N]: ')).strip().upper()
    if opção in 'Nn':
        break
lista.sort()
print(f'\nVocê digitou os valores {lista}\n')

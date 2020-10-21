lista=[]
listapar=[]
listaimpar=[]

while True:
    lista.append(int(input('Digite um número: ')))
    opção=str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if opção in 'Nn':
        break

for c in range(0,len(lista)):
    if lista[c] % 2 == 0:
        listapar.append(lista[c])
    else:
        listaimpar.append(lista[c])
print(f'\nA lista completa é {lista}')
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimpar}\n')

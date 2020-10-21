lista=[]

for cont in range(1,6):
    n=int(input('Digite um valor: '))
    if cont == 1 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos=0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado à posição {pos+1} da lista...')
                break
            pos+=1
print(f'\nOs valores digitados em ordem foram {lista}\n')

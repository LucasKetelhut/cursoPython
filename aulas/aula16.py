lanche=('Hambúrguer','Suco','Pizza','Pudim')
#tuplas são imutáveis
print(lanche[2:])
print(lanche[:2])
print(lanche[-1])
print(len(lanche))

#mostrar elementos
for c in lanche:
    print(c)

#mostrar posição
for c in range(0,len(lanche)):
    print(f'{lanche[c]} na posição {c}')

#mostrar em ordem
print(sorted(lanche))

#quantas vezes aparece na tupla
print(lanche.count('Pudim'))

#em que posição está
print(lanche.index('Pudim'))

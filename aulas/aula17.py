num=[2,5,9,1]
num[2]=3
print(num)
#adicionando valores
num.append(7)
print(num)
#colocando em ordem
num.sort()
print(num)
#ordem reversa
num.sort(reverse=True)
print(num)
#número de elementos
len(num)
#adicionar valor em posição
num.insert(2,2)
print(num)
#removendo elemento 
num.pop(2)
print(num)
#removendo a primeira ocorrencia do valor
num.remove(2)
print(num)

valores=[]

for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for valor in valores:
    print(f'{valor}...',end='')
print('\n')

galera=[]
dado=[]

for c in range(0,3):
    dado.append(str(input('Nome: ')).strip())
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #cópia para a lista principal
    dado.clear() #limpando a lista secundaria

for pessoa in galera:
    if pessoa[1] >=21:
        print(f'{pessoa[0]} é maior de idade.')
    else:
        print(f'{pessoa[0]} é menor de idade.')

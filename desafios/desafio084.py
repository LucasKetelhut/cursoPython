princ=[]
temp=[]
maior=menor=cont=0

while True:
    temp.append(str(input('Nome: ')).strip())
    temp.append(float(input('Peso: ')))
    if cont==0:
        maior=menor=temp[1]
    else:
        if temp[1] > maior:
            maior=temp[1]
        if temp[1] < menor:
            menor=temp[1]
    princ.append(temp[:])
    cont+=1
    temp.clear()
    opção=str(input('Quer continuar? [S/N]: '))
    if opção in 'Nn':
        break

print(f'\nForam cadastradas {cont} pessoas.')
print(f'O maior peso foi de {maior}kgs. Peso de ',end='')
for pessoa in princ:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}] ',end='')
print()
print(f'O menor peso foi de {menor}kgs. Peso de ',end='')
for pessoa in princ:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}] ',end='')
print('\n')

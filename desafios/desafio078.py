lista=[]

for cont in range(1,6):
    lista.append(int(input(f'Insira um valor para a posição {cont}: ')))    

maior=max(lista)
menor=min(lista)

print(f'Os valores digitados foram: {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ',end='')
for i,v in enumerate(lista):
    if v == maior:
        print(f'{i+1}...',end='')
print()
print(f'O menor valor digitado foi {min(lista)} nas posições ',end='')
for i,v in enumerate(lista):
    if v == menor:
        print(f'{i+1}...',end='')
print()

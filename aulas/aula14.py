i=1
par=impar=0
while i != 0:
    i=int(input('Digite um valor: '))
    if i !=0:
        if i % 2 == 0:
            par+=1
        else:
            impar+=1
print(f'Você digitou {par} números pares e {impar} números ímpares!')

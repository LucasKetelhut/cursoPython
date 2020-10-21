primeiro=int(input('Insira o primeiro termo da PA: '))
razão=int(input('Insira a razão da PA: '))
i=0 

while i < 10:
    print(primeiro,end=' → ')
    primeiro += razão
    i += 1
print('FIM')

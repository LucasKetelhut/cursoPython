primeiro=int(input('Insira o primeiro termo da PA: '))
razão=int(input('Insira a razão da PA: '))
décimo=primeiro+(10-1)*razão

for i in range(primeiro,décimo + razão,razão):
    print(i,end= ' → ')
print('FIM!')

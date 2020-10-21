primeiro=int(input('Insira o primeiro termo da PA: '))
razão=int(input('Insira a razão da PA: '))
i=0 
total=0
escolha=10
while escolha != 0:
    total+=escolha
    while i < total:
        print(primeiro,end=' → ')
        primeiro += razão
        i += 1
    print('PAUSA')
    escolha=int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')

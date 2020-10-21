sexo=str(input('Digite o seu sexo [M/F]: ')).upper()

while sexo != 'M' and sexo != 'F':
    print('Opção inválida. ')
    sexo=str(input('Digite o seu sexo [M/F]: ')).upper()
if sexo == 'M':
    print('Aprovado!')
elif sexo == 'F':
    print('Aprovada!')

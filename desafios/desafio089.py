ficha=[]

while True:
    nome=str(input('Nome: ')).strip()
    n1=float(input('Nota 1: '))
    n2=float(input('Nota 2: '))
    media=(n1+n2)/2
    ficha.append([nome,[n1,n2],media])
    opção=str(input('Quer continuar? [S/N]: '))
    if opção in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*25)

for i, aluno in enumerate(ficha):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-'*25)
    opç=int(input('Mostrar notas de qual aluno? [999 para parar]: '))
    if opç == 999:
        break
    if opç <= len(ficha) - 1:
        print(f'Notas de {ficha[opç][0]} são {ficha[opç][1]}')
print('<<< VOLTE SEMPRE >>>')

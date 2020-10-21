import time
n1=int(input('Digite o primeiro valor: '))
n2=int(input('Digite o segundo valor: '))

opção=0

while opção != 5:
    print('''\nO QUE DESEJA FAZER COM ESSES DOIS NÚMEROS?
[1]-SOMAR
[2]-MULTIPLICAR
[3]-MAIOR
[4]-NOVOS NÚMEROS
[5]-SAIR DO PROGRAMA\n''')
    opção=int(input('Sua escolha: '))
    if opção == 1:
        print(f'{n1} + {n2} = {n1+n2}')
        time.sleep(2)
    elif opção == 2:
        print(f'{n1} x {n2} = {n1*n2}')
        time.sleep(2)
    elif opção == 3:
        if n1 >= n2:
            print(f'O maior entre {n1} e {n2} é {n1}')
        else:
            print(f'O maior entre {n1} e {n2} é {n2}')
        time.sleep(2)
    elif opção == 4:
            n1=int(input('Digite o primeiro valor: '))
            n2=int(input('Digite o segundo valor: '))
            time.sleep(2)
print('VOCÊ ESCOLHEU SAIR!\nATÉ LOGO!')

num=int(input('Digite um número inteiro: '))
print('Qual será a base de conversão?')
print('Opção 1 para binário\nOpção 2 para octal\nOpção 3 para hexadecimal')
opcao=int(input('Opção escolhida: '))

if opcao == 1:
    num=bin(num)
    print(num[2:])
elif opcao == 2:
    num=oct(num)
    print(num[2:])
elif opcao == 3:
    num=hex(num)
    print(num[2:])
else:
    print('Opção inválida')

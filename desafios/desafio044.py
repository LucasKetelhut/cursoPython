valor=float(input('Qual o preço do produto: R$'))
print('Qual vai ser a opção de pagamento?')
print('OPÇÃO 1: À VISTA DINHEIRO/CHEQUE (10% DESCONTO)')
print('OPÇÃO 2: À VISTA CARTÃO (5% DESCONTO)')
print('OPÇÃO 3: EM ATÉ 2X NO CARTÃO (PREÇO NORMAL)')
print('OPÇÃO 4: EM 3X OU MAIS NO CARTÃO (20% JUROS)')
opcao=int(input(''))

if opcao==1:
    valor= valor-(0.1 * valor)
    print('Valor a ser pago: R${:.2f}'.format(valor).replace('.',','))
elif opcao==2:
    valor=valor-(0.05*valor)
    print('Valor a ser pago: R${:.2f}'.format(valor).replace('.',','))
elif opcao==3:
    print('Valor a ser pago: R${:.2f}'.format(valor).replace('.',','))
elif opcao==4:
    valor=valor+(0.2*valor)
    print('Valor a ser pago: R${:.2f}'.format(valor).replace('.',','))
else:
    print('Opção inválida')

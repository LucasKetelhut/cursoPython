casa=float(input('Insira o valor da casa: R$'))
salario=float(input('Insira o salário do comprador: R$'))
anos=int(input('Em quantos anos ele irá pagar: '))

meses=anos * 12
gasto=casa/meses

if (gasto > (0.3 * salario)):
    print('O gasto mensal será de R${:.2f} durante os próximos {} meses\nIsso é superior a 30% do seu salário!'.format(gasto,meses).replace('.',','))
    print('Impossível fincanciar a casa.')
else:
    print('O gasto mensal será de R${:.2f} durante os próximos {} meses'.format(gasto,meses).replace('.',','))
    print('Você tem a opção de financiar esta casa!')

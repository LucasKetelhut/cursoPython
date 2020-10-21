nome=opção=maisbarato=''
preço=total=maisdemil=cont=maisbaratopreço=0

print('-'*25)
print('          LOJA')
print('-'*25)

while True:
    nome=str(input('Nome do produto: ')).strip()
    preço=float(input('Preço: R$'))
    if cont==0:
        maisbarato=nome
        maisbaratopreço=preço
    if preço < maisbaratopreço:
        maisbarato=nome
        maisbaratopreço=preço
    cont+=1
    total+=preço
    if preço > 1000:
        maisdemil+=1
    opção=str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while opção != 'S' and opção != 'N':
        opção=str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if opção == 'N':
        break
print('\n---------- FIM DO PROGRAMA ----------')
print(f'\nO valor total da compra foi de R${total:.2f}'.replace('.',','))
print(f'Temos {maisdemil} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {maisbarato}, custando apenas R${maisbaratopreço:.2f}!\n'.replace('.',','))

produtos=('Lápis',1.75,'Borracha',2,'Caderno',15.90,'Estojo',25,'Mochila',120,'Livro',34.90)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for c in range(0,len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}',end='')
    else:
        print(f'R${produtos[c]:>7.2f}')

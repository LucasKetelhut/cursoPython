tabela=('Atlético-MG','Flamengo','Corinthians','Palmeiras','Fluminense',
'América-MG','São Paulo','Grêmio','Vasco','Internacional',
'Botafogo','Sport','Cruzeiro','Vitória','Santos','Chapecoense',
'Atlético-PR','Bahia','Ceará','Paraná Clube')
print(f'Tabela do Brasileirão 2018 na sexta rodada: {tabela}')
print('=-'*30)
print(f'Os 5 primeiro colocados são: {tabela[0:5]}')
print('=-'*30)
print(f'Os últimos 4 colocados são: {tabela[-4:]}')
print('=-'*30)
print(f'Os time do Brasileirão 2018 em ordem alfabética: {sorted(tabela)}')
print('=-'*30)
chape=tabela.index('Chapecoense') + 1
print(f'A Chapecoense se encontra na {chape}ª posição!')

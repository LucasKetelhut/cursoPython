pessoas={'nome':'Lucas','sexo':'M','idade':19}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print('-'*30)
#laços com key value e items
for key in pessoas.keys():
    print(key)
for values in pessoas.values():
    print(values)
for key,value in pessoas.items():
    print(f'{key} = {value}')

#apagar 
del pessoas['sexo']
#substituindo
pessoas['nome'] = 'Giovanna'
print('-'*30)
#adicionando elemento
pessoas['peso']=35.6
#listas
estado={}
brasil=[]
for c in range(0,3):
    estado['uf']=str(input('Unidade Federativa: ')).strip()
    estado['sigla']=str(input('Sigla do Estado: ')).strip()
    brasil.append(estado.copy())

for estado in brasil:
    for v in estado.values():
        print(f'{v}',end=' ')
    print()

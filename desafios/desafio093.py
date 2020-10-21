dados={'Nome':str(input('Nome do Jogador: ')).strip()}
partidas=int(input('Quantas partidas ele jogou: '))
gols=[]
total=0
for c in range(1,partidas+1):
    marcados=int(input(f'Quantos gols na partida {c}: '))
    gols.append(marcados)
    total+=marcados
dados['Gols']=gols
dados['Total']=total
print('-'*30)
print(dados)
print('-'*30)
for key,value in dados.items():
    print(f'O campo {key} tem o valor {value}.')
print('-'*30)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')
for i,v in enumerate(gols):
    print(f'=> Na partida {i+1}, fez {v} gols.')
print(f'O jogador fez um total de {total} gols.')

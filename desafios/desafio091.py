import random
import time
import operator

resultado={'Jogador 1':random.randint(1,6),'Jogador 2':random.randint(1,6),
'Jogador 3':random.randint(1,6),'Jogador 4':random.randint(1,6)}

ranking=[]

print('Valores sorteados:')
for key,value in resultado.items():
    print(f'O {key} tirou {value} no dado.')
    time.sleep(1)

print('-'*30)
print('Ranking dos jogadores:')
ranking=sorted(resultado.items(),key=operator.itemgetter(1),reverse=True)

for i,v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    time.sleep(1)

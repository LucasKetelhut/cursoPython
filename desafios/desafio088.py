import random
import time

sorteio=[]
jogos=[]
num=total=0

print('-'*40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-'*40)
escolha=int(input('Quantos jogos você quer que eu sorteie? '))
print()
print('-='*3,f' SORTEANDO {escolha} JOGOS ','=-'*3)
print()
while total < escolha:
    cont=0
    while True:
        num=random.randint(1,60)
        if num not in sorteio:
            sorteio.append(num)
            cont+=1
        if cont >= 6:
            break
    sorteio.sort()
    jogos.append(sorteio[:])
    sorteio.clear()
    total+=1

for i,v in enumerate(jogos):
    print(f'Jogo {i+1}: {v}')
    time.sleep(1)
print()
print('-='*5,'< BOA SORTE! >','=-'*5)
print()

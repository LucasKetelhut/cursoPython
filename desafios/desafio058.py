import random
import time
computador=random.randint(0,10)
palpites=1

print('*-'*25,end='*\n')
print('VOU PENSAR EM UM NÚMERO DE 0 A 10, TENTE ADIVINHAR!')
print('*-'*25,end='*\n')
time.sleep(1)
print('VAMOS LÁ!'),time.sleep(1)
print('PENSANDO...'),time.sleep(1)

jogador=int(input('Tente acertar! Em qual número eu pensei: '))

while jogador != computador:
    jogador=int(input('Você errou! Tente novamente: '))
    palpites+=1

print('Muito bem!! Você conseguiu acertar!'),time.sleep(0.5)
print('CALCULANDO NÚMERO DE TENTAVIAS...'),time.sleep(1)
print(f'Para me derrotar você precisou de {palpites} tentativa(s)! Legal!')

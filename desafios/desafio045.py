import random
import time
print('-+-'*7)
print('VAMOS JOGAR JOKENPÔ!')
print('-+-'*7)
print('ESCOLHA A SUA JOGADA!\n1 = PEDRA\n2 = PAPEL\n3 = TESOURA')
jogador=(input())
jogadas=['PEDRA!','PAPEL!','TESOURA!']
computador=random.choice(jogadas)

if jogador == '1':
    jogador = 'PEDRA!'
elif jogador == '2':
    jogador = 'PAPEL!'
elif jogador == '3':
    jogador = 'TESOURA!'

if jogador =='PEDRA!' and computador == 'PEDRA!':
    print('JÓ...')
    time.sleep(1)
    print('KEN...')
    time.sleep(1)
    print('PÔ!!!')
    time.sleep(0.5)
    print(f'VOCÊ JOGOU {jogador}\nEU JOGUEI {computador}\nEMPATAMOS!') 
elif jogador =='PAPEL!' and computador == 'PAPEL!':
    print('JÓ...')
    time.sleep(1)
    print('KEN...')
    time.sleep(1)
    print('PÔ!!!')
    time.sleep(0.5)
    print(f'VOCÊ JOGOU {jogador}\nEU JOGUEI {computador}\nEMPATAMOS!')
elif jogador=='TESOURA!' and computador == 'TESOURA!':
    print('JÓ...')
    time.sleep(1)
    print('KEN...')
    time.sleep(1)
    print('PÔ!!!')
    time.sleep(0.5)
    print(f'VOCÊ JOGOU {jogador}\nEU JOGUEI {computador}\nEMPATAMOS!') 
elif jogador=='PEDRA!' and computador == 'PAPEL!':
    print('JÓ...')
    time.sleep(1)
    print('KEN...')
    time.sleep(1)
    print('PÔ!!!')
    time.sleep(0.5)
    print(f'VOCÊ JOGOU {jogador}\nEU JOGUEI {computador}\nEU VENCI! MAIS SORTE NA PRÓXIMA!')
elif jogador=='PEDRA!' and computador == 'TESOURA!':
    print('JÓ...')
    time.sleep(1)
    print('KEN...')
    time.sleep(1)
    print('PÔ!!!')
    time.sleep(0.5)
    print(f'VOCÊ JOGOU {jogador}\nEU JOGUEI {computador}\nDROGA! FUI DERROTADO! VOCÊ VENCEU, PARABÉNS!') 
elif jogador=='PAPEL!' and computador == 'PEDRA!':
    print('JÓ...')
    time.sleep(1)
    print('KEN...')
    time.sleep(1)
    print('PÔ!!!')
    time.sleep(0.5)
    print(f'VOCÊ JOGOU {jogador}\nEU JOGUEI {computador}\nDROGA! FUI DERROTADO! VOCÊ VENCEU, PARABÉNS!')
elif jogador=='PAPEL!' and computador == 'TESOURA!':
    print('JÓ...')
    time.sleep(1)
    print('KEN...')
    time.sleep(1)
    print('PÔ!!!')
    time.sleep(0.5)
    print(f'VOCÊ JOGOU {jogador}\nEU JOGUEI {computador}\nEU VENCI! MAIS SORTE NA PRÓXIMA!')
elif jogador=='TESOURA!' and computador == 'PEDRA!':
    print('JÓ...')
    time.sleep(1)
    print('KEN...')
    time.sleep(1)
    print('PÔ!!!')
    time.sleep(0.5)
    print(f'VOCÊ JOGOU {jogador}\nEU JOGUEI {computador}\nEU VENCI! MAIS SORTE NA PRÓXIMA!')
elif jogador=='TESOURA!' and computador== 'PAPEL!':
    print('JÓ...')
    time.sleep(1)
    print('KEN...')
    time.sleep(1)
    print('PÔ!!!')
    time.sleep(0.5)
    print(f'VOCÊ JOGOU {jogador}\nEU JOGUEI {computador}\nDROGA! FUI DERROTADO! VOCÊ VENCEU, PARABÉNS!')      
 
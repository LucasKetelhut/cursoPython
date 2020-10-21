import random

tupla=((random.randint(0,10)),(random.randint(0,10)),(random.randint(0,10)),(random.randint(0,10)),(random.randint(0,10)))

print(f'Os valores sorteados foram: {tupla}')
print(f'O maior valor sorteado foi: {sorted(tupla)[-1]}')
print(f'O menor valor sorteado foi: {sorted(tupla)[0]}')

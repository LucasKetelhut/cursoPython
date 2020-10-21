frase=str(input('Digite uma frase: ')).strip().lower().replace(' ','')
inverso=''

for i in range(len(frase)-1,-1,-1):
    inverso += frase[i]

print(f'O inverso de {frase} é {inverso}')

if inverso == frase:
    print('A frase digitada é um PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!')

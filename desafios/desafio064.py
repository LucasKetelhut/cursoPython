n=0
quantos=0
soma=0

while n != 999:
    n=int(input('Digite um número [999 para parar]: '))
    if n != 999:
        quantos+=1
        soma+=n
print(f'Foram digitado {quantos} números e a soma entre eles é {soma}.')

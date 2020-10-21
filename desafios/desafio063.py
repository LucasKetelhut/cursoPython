# 0 - 1 - 1 
# t1  t2  t3
n=int(input('Quantos termos você quer da Sequência de Fibonacci: '))
termo1=0 #são 
termo2=1 #definidos automaticamente
contador=3

print(f'{termo1} → {termo2}',end='')

while contador <= n:
    termo3=termo1+termo2
    print(f' → {termo3}',end='')
    termo1=termo2
    termo2=termo3
    contador+=1
print(' → FIM')

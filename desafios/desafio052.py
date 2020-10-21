divisores=0
n=int(input('Digite um número inteiro: '))

for i in range(1,n+1):
    if(n % i) == 0:
        divisores += 1

if divisores == 2:
    print(f'O número {n} é primo!')
else:
    print(f'O número {n} não é primo!')

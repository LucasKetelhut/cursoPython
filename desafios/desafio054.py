import datetime
maiores=0
menores=0
anoatual= datetime.date.today().year

for i in range(1,8):
    ano=int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))
    idade=anoatual-ano
    if idade>=21:
        maiores+=1
    elif idade<21:
        menores+=1
print(f'Dessas 7 pessoas, {maiores} atingiram a maioridade e {menores} ainda estão na menoridade!')

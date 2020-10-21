import datetime
ano=int(input('Insira o ano de nascimento do atleta: '))
anoatual= datetime.date.today().year

print(f'O atleta tem {anoatual-ano} anos')

if anoatual-ano <=9:
    print('MIRIM')
elif anoatual-ano <=14:
    print('INFANTIL')
elif anoatual-ano <=19:
    print('JUNIOR')
elif anoatual-ano <=20:
    print('SÊNIOR')
else:
    print('MASTER')

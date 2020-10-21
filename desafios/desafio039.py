import datetime
ano=int(input('Digite o ano de nascimento: '))
anoatual= datetime.date.today().year

print(f'Quem nasceu em {ano} está com {anoatual-ano} anos em {anoatual}')

if anoatual-ano==18:
    print('Está na hora de se alistar!')
elif anoatual-ano<18:
    dif=18-(anoatual-ano)
    print('Ainda não está na hora de se alistar.')
    print(f'Falta(m) {dif} ano(s) para o seu alistamento obrigatório!')
elif anoatual-ano>18:
    dif=(anoatual-ano)-18
    print('Você já passou do período de alistamento!')
    print(f'O seu alistamento obrigatório foi a {dif} ano(s) atrás!')

import datetime
dados={'Nome':str(input('Nome: ')).strip(),'Idade':int(input('Ano de Nascimento: ')),
'Ctps':int(input('Carteira de Trabalho ["0" se não possui]: '))}
anoatual=datetime.date.today().year

if dados['Ctps'] != 0:
    dados['Contratação']=int(input('Ano de contratação: '))
    dados['Salário']=float(input('Salário: R$'))
    dados['temp']= dados['Contratação'] - dados['Idade']
    dados['Aposentadoria']= dados['temp']+35
    del dados['temp']

dados['Idade']= anoatual - dados['Idade']

print('-'*30)

for key,value in dados.items():
    print(f'{key} tem o valor {value}')

aluno={}
aluno['Nome']=str(input('Nome: ')).strip()
aluno['Média']=float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Média'] >=7:
    aluno['Situação']='Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação']='Recuperação'
else:
    aluno['Situação']='Reprovado'
print('-'*30)
for key,value in aluno.items():
    print(f'{key} é igual a {value}')

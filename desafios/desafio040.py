n1=float(input('Insira a primeira nota: '))
n2=float(input('Insira a segunda nota: '))
m=(n1+n2)/2

if m<5:
    print('Média: {:.1f}\nAluno REPROVADO!'.format(m))
elif m>=5 and m<7:
    print('Média: {:.1f}\nAluno de RECUPERAÇÃO!'.format(m))
elif m>=7:
    print('Média: {:.1f}\nAluno APROVADO!'.format(m))

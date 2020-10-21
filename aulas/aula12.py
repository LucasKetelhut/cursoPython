nome=str(input('Qual é o seu nome? ')).strip()

if nome == 'Lucas':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Eduarda Giovanna Júlia':
    print('Belo nome feminino!')
else:
    print('Seu nome é normal.')

print(f'Tenha um bom dia, {nome}!')

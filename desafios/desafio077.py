palavras=('arroz','curso','programa','linguagem','jogos','macarronada','agua','tenis')

for letras in palavras:
    print(f'\nNa palavra {letras.upper()} temos ',end='')
    for palavras in letras:
        if palavras.lower() in 'aeiou':
            print(palavras,end=' ')
print('\n')

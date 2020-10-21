peso=float(input('Insira o peso: '))
altura=float(input('Insira a altura: '))

imc= peso/(pow(altura,2))

print('IMC = {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc <40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbida')

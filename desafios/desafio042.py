r1=float(input('Primeiro lado: '))
r2=float(input('Segundo lado: '))
r3=float(input('Terceiro lado: '))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os lados citados PODEM formar um triângulo ',end ='')
     
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')

else:
    print('Os lados citados NÃO PODEM formar um triângulo!')

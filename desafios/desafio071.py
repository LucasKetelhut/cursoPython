print('='*30)
print('       Banco do Lukinha')
print('='*30)

valor=int(input('Qual o valor que deseja sacar? [50/20/10/1]: R$'))
total=valor
ced=50
totalced=0

while True:
    if total >= ced:
        total-=ced
        totalced+=1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        totalced=0    
        if total == 0:
            break            
print('='*30)
print('\nTenha um bom dia!\n')

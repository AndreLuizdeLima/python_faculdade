def somar(num1,num2):
    resultado = num1 + num2
    return resultado

def diminuir(num1,num2):
    resultado = num1 - num2
    return resultado
    
    

print('Opcoes')
print('1: somar:')
print('2: diminuir:')
print('')
decisao = int(input('Sua escolha: '))
print('')
    
if decisao == 1:
    x = int(input('numero1: '))
    y = int(input('numero2: '))
    print(somar(x,y))
if decisao == 2:    
    x = int(input('numero1: '))
    y = int(input('numero2: '))
    print(diminuir(x,y))       

        
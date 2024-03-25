print('inicio do programa Calculadora')

print('')

num1 = int(input('Forneca um numero: '))
num2 = int(input('Forneca um segundo numero: '))

print('')

print('Agora selecione a operação a ser realizada')

print('Adição = 1')
print('Subitração = 2')
print('Multiplicacao = 3')
print('Divisao = 4')

print('')

operacao = int(input('selecione sua opcao: '))


if operacao == 1:
    soma = num1 + num2
    print(f'A soma dos dois numero:  {soma}')

if operacao == 2:
    subi = num1 - num2
    print(f'A subitracao entre os dois numeros é:  {subi}')
    

if operacao == 3:
    multi = num1 * num2
    print(f'A multiplicacao entre os dois numeros é:  {multi}')
    


if operacao == 4:
    divi = num1 / num2
    print(f'A divisao entre os dois numeros é:  {divi}')

else:
    print('opção digitada invalidada')


print('*** [Caixa Eletronico] ***')
print('')
print('Nesse programa vamos calcular quantas notas devem sair do caixa')
print('De acordo com a quantidade informada sendo o mais eficiente possivel')
print('')
valor = int(input('Digite o valor solicitado:'))
total = valor
print('')

#acredito que dessa forma fazer um filtro na quantidade possa ser util

#filtro notas de 100
notasQuantidade100 = valor // 100
#saber quando descontar a a quantidade de notas de 100
valorDescontado100 = notasQuantidade100 * 100
#descontar a quantidade
valor = valor - valorDescontado100

notasQuantidade50 = valor // 50
valorDescontado50 = notasQuantidade50 * 50
valor = valor - valorDescontado50

notasQuantidade20 = valor // 20
valorDescontado20 = notasQuantidade20 * 20
valor = valor - valorDescontado20

notasQuantidade10 = valor // 10
valorDescontado10 = notasQuantidade10 * 10
valor = valor - valorDescontado10

notasQuantidade5 = valor // 5
valorDescontado5 = notasQuantidade5 * 5
valor = valor - valorDescontado5

notasQuantidade2 = valor // 2
valorDescontado2 = notasQuantidade2 * 2
valor = valor - valorDescontado2


print(f'A forma mais Eficiente de entregar {total} seria com:')
print(f'{notasQuantidade100} notas de 100 reais')
print(f'{notasQuantidade50} notas de 50 reais')
print(f'{notasQuantidade20} notas de 20 reais')
print(f'{notasQuantidade10} notas de 10 reais')
print(f'{notasQuantidade5} notas de 5 reais')
print(f'{notasQuantidade2} notas de 2 reais')






listaCompra = [ 'laranja', 'maça', 'abacate', 'morango']

print(listaCompra)
    
listaCompra.append('kiwi')

print(listaCompra)

print(listaCompra[1])

for i in listaCompra:
    print(i)
    
num = len(listaCompra)

print(listaCompra[num - 1])

listaCompra.pop(1)
listaCompra.remove('laranja')

print(listaCompra)
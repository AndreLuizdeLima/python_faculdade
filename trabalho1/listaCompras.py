print('iniciando o programa Lista de Compras')
i = 1

listaCompras = []

while i == 1:
    print('Selecione sua operação:')
    print('')
    print('1: Adicionar item ')
    print('2: Excluir item ')
    print('3: Visualizar ')
    print('4: Sair do programa ')
    print('')
    decisao = input('Escolha: ')
    
    if decisao == '1':
        add = input('Adicionar item: ')
        listaCompras.append(add)
        print('')
        null = input('')

    if decisao == '2':
        rem = input('Informe o que deseja remover: ')
        listaCompras.remove(rem)
        print('')
        null = input('')
        
    if decisao == '3':
        print('')
        print('==== Produtos: ====')
        for a in listaCompras:
            print(a)      
        print('=== === === === ')
        print('')
        null = input('')
    
    if decisao == '4':
        print('==== Saindo do programa ====')
        i+=1
        
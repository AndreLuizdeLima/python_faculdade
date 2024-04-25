print('Iniciando sistema de cadastro de usuarios')

i = 1

usuarios = []

while i == 1:
    print('Opcoes')
    print('1: Novo usuario:')
    print('2: Listar usuario:')
    print('3: Editar Usuario:')
    print('4: Sair do programa:')
    print('')
    decisao = int(input('Sua escolha: '))
    print('')
    
    if decisao == 1:
        print('')
        print('Iniciando cadastro de usuarios')
        print('')

        user = {}

        user['nome'] = input('Seu nome: ')
        user['cpf'] = input('Seu CPF: ')
        user['cep'] = input('Seu CEP: ')
        
        usuarios.append(user)
        
        print('')
        print('')
        

    if decisao == 2:
        k = 0
        for j in usuarios:
            print(f'Usuario {k}')
            for key in j:
                print(f'{key} , {j[key]}')
            k+=1
            print('')    
            
    if decisao == 3:
        pesquisa = input('Informe o nome de qual usuario deseja editar:')
        for l in usuarios:
            if pesquisa == usuarios['cpf']:
                usuarios['cpf'] = input('Informe novo Cpf: ')   
        

        
        
    if decisao == 4:
        i+=1
        
   
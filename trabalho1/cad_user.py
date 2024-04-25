print('Iniciando sistema de cadastro de usuarios')

i = 1

usuarios = []

while i == 1:
    print('Opcoes')
    print('1: Novo usuario')
    print('2: Listar usuario')
    print('3: Sair do programa')
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
        k = 1
        for j in usuarios:
            print(f'Usuario {k}')
            for key in j:
                print(f'{key} , {j[key]}')
            k+=1
            print('')    
            
        
    if decisao == 3:
        i+=1
        
   
print('======= iniciando cadastro de pessoa =======')
print('Iremos cadastrar alguns dados')


cadastro = {    
}

cadastro['nome'] = input('Seu nome:')
cadastro['cpf'] = input('Seu CPF:')
cadastro['cep'] = input('Seu CEP:')

print(cadastro)
print('')

for key in cadastro.keys():
    print(key,cadastro[key]) 
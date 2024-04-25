pessoa = {
    'nome':'Andre',
    'cpf':'99999999999',
    'cep':'85509370'
}

print(pessoa['nome'])
print(pessoa.get('name'))

pessoa['name'] = 'Andre Luiz'
print(pessoa['name'])
del pessoa['name']
print(pessoa.get('name'))
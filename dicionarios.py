# Criando dicionários

dic = {
    'nome': 'Devid',
    'idade': 18,
    'altura': 1.69
}

print(dic)

# Acessando elementos

print(dic['nome'], dic['idade'])

# Adicionando elementos

dic['programador'] = True

print(dic)

# Percorrendo um dicionário

for key in dic:
    print(key, dic[key])

# Verificando a existência de chaves

print('peso' in dic)
print('programador' in dic)

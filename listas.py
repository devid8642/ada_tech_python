# Criando listas

lista = [1, 2, 3, 'a', 'devid', 9.45, 12.5, True, False]

# Indexação

print(lista[0])
print(lista[3])
print(lista[-1])

# Slice

print(lista[:5])
print(lista[::2])

# Percorrendo os elementos da lista

for elemento in lista:
    print(elemento)

for i in range(len(lista)):
    print(lista[i])

# Métodos de Listas

lista = [1, 5, 6, 2, 2, 7, 8, 1, 19]

# Append

print(f'Lista antes do append: {lista}')

lista.append(200)

print(f'Lista após o append: {lista}')

# Insert

lista.insert(5, 50)

print(f'Lista após o insert: {lista}')

# Pop

lista.pop()

print(f'Lista após o pop: {lista}')

# Remove

lista.remove(2)

print(f'Lista após o remove: {lista}')

# Index

print(f'Index do item 2 da lista: {lista.index(2)}')

# Sort

lista.sort()

print(f'Lista após o sort: {lista}')

# Sum

print(f'Soma de todos os números da lista: {sum(lista)}')

# Max

print(f'Maior número dessa lista: {max(lista)}')

# Min

print(f'Menor número dessa lista: {min(lista)}')

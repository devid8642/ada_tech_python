# Conversão de tipos
'''
    Funções de conversão:
    str()
    int()
    float()
    bool()
'''

n1 = '10'
n2 = '20'

print(n1, type(n1))
print(n2, type(n2))
print(n1 + n2)

n1 = int(n1)
n2 = int(n2)

print(n1, type(n1))
print(n2, type(n2))
print(n1 + n2)

# o input lê como str por padrão

n = input('Digite um número: ')
print(n, type(n))
print(int(n) ** 2)

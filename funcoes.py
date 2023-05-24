# Criando funções

def saudacao():
    print('Seja bem vindo(a)!')

saudacao()

# Criando funções com parâmetros

def saudacao(nome):
    print(f'Seja bem vindo(a) {nome}')

saudacao('Devid')

# Criando funções com parâmetros opcionais

def saudacao(nome = ''):
    if nome == '':
        print('Seja bem vindo(a)!')
    else:
        print(f'Seja bem vindo(a) {nome}')

saudacao('Devid')
saudacao()

# Funções com retorno

def soma(num1, num2):
    return num1 + num2

print(soma(20, 42))

# Exercício da calculadora

def calcula(num1, num2, op = '+'):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    return num1 / num2

print(calcula(2, 3, '+'))
print(calcula(34, 1, '-'))
print(calcula(45, 21, '*'))

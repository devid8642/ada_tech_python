# Condicionais

idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')

# Exercício da média de um aluno

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2)/2

if media >= 7:
    print('Aprovado(a)')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado(a)')

# Segundo exercício: média e presença

media = 10
presenca = 100

if media >= 7 and presenca >= 70:
    print('Aprovado(a)')
else:
    print('Reprovado(a)')

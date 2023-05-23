from random import randint

# Exercicío 1: Jogo da adivinhação

numero_aleatorio = randint(0, 20)

numero_escolhido = int(input('Digite um número inteiro entre 0 e 20: '))

while numero_escolhido != numero_aleatorio:
    print('Você errou tente novamente...')
    numero_escolhido = int(input('Digite um número inteiro entre 0 e 20: '))

print('Você acertou')

# Exercício 2: Repetição com contador

c = 0

while c < 5:
    print(c)
    c += 1

print('Fim do programa')

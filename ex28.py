from random import randint

computador = randint(0, 5)
print('já escolhi o meu número. Qual você acha que é? \n')

jogador = int(input('Escolha um número entre 0 e 5: '))
if jogador == computador:
    print('Você acertou! o número é: {}'.format(jogador))
else:
    print('Você errou! o número era o: {}'.format(computador))

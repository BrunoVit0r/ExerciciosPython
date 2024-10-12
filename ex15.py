# carro custa R$60,00 por dia e R$0,15 por km rodado

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

resultado = (dias * 60) + (km * 0.15)

print('O total a pagar é: R${:.2f}'.format(resultado))
distancia = float(input('Digite a distância da viagem: '))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print('O preço da passagem é de R$ {:.2f} reais.'.format(preco))
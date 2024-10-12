velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade-80) * 7
    print('Você foi multado por exceder o limite de 80 km/h. Deve pagar R$ {:.2f} reais'.format(multa))
print('Tenha um bom dia! Dirija com segurança.')
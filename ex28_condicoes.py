tempo = int(input('Seu carro é qual ano? '))
calculo = 2024 - tempo

if calculo <= 5:
    print('Seu carro tem {} anos, ainda está novo! \n'.format(calculo))
elif calculo > 6 and calculo <= 10:
    print('Seu carro tem {} anos, está na hora de pensar em outro! \n'.format(calculo))
else:
    print('Seu carro tem {} anos, passou da hora de trocar! \n'.format(calculo))

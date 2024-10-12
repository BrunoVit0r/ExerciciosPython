nome = str(input('Digite seu nome completo: ')).strip()
print('Estamos analisando seu nome ... \n' )

print('Seu nome em Maiúsculas é {} \n'.format(nome.upper()))
print('Seu nome em Minúsculas é {} \n'.format(nome.lower()))
print('O tamanho do seu nome é de {} letras \n'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras \n'.format(nome.find(' ')))

separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras \n'.format(separa[0], len(separa[0])))
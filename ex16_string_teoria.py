frase = 'Curso em Video Python'

print(frase)
print(frase[9])
print(frase[9:14])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('deo'))

print(frase.split())
print('-'.join(frase))
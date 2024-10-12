salario = float(input('Digite seu salário: R$ '))
salarioDesc = salario - (salario * 5 / 100)
salarioAcresc = salario + (salario * 15 / 100)
print('O salario é: R$ {:.2f}, com desconto de 5% é: R$ {:.2f} e com acréscimo de 15% é: R$ {:.2f} \n'.format(salario, salarioDesc, salarioAcresc))

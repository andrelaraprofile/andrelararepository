# Faça um programa que leia a validade das informações: 
# a. Idade: entre 0 e 150 
# b. Salário: maior que 0
# c. Sexo: M, F ou Outro
idade= int(input('Qual a sua idade?'))
if idade > 0 and idade <= 150:
    print('Informação válida')
else:
    idade < 0 and idade >150
    print ('Informação inválida')

salario= float(input('Qual o seu salário: '))
if salario > 0:
    print ('Informação válida')
else:
    salario = 0
    print ('informação inválida')

sexo = input('Qual o seu genêro? (use: M para masculino F para feminino ou O para outro):')
if sexo == 'M' or  sexo == 'F' or sexo == 'O':
    print ('Informação válida')
else:
    print ('Informação inválida')
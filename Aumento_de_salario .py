Salario = float(input('Qual e o salario do funcionario? R$'))
Porcentagem = int(input('Quantos por cento sera aumentado? (Digite somente o valor) '))
Aumento = Salario + (Salario * Porcentagem / 100) 
print(f'Um funcionario que ganhava R${Salario:.2f}, com {Porcentagem}% de aumento, passará a receber R${Aumento:.2f}')
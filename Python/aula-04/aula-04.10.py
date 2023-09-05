# DESAFIO 013 FAÇA UM ALGORÍTIMO QUE MOSTRE O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO COM 15% DE AUMENTO

salario = float(input(' Qual é seu salário atual?: R$:'))
aumento = salario * 0.15
novo_salario = salario + aumento
print(' Seu salário atual é R$:{:.3f}\n Seu novo salário com aumento de 15% é R$:{:.3f}'.format(salario, novo_salario))
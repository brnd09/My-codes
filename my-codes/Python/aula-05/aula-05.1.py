import math
# DESAFIO 016 - CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA A SUA PORÇÃO INTEIRA
# EXEMPLO: DIGITE UM NÚMERO: 6.127 / O NÚMERO 6.127 TEM A PARTE INTEIRA 6

n1 = float(input('Escreva qualquer número, para mostrar sua porção inteira: '))
inter = (math.trunc(n1))
print(f'O número {n1} tem a parte inteira {inter}')
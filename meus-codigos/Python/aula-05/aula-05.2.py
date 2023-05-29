import math
# DESAFIO 017 - FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIÂNGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA

co = float(input('escreva o valor do cateto oposto: '))
ca = float(input('escreva o valor do cateto adjacente: '))
hip = math.hypot (co, ca)
print(f'A soma do cateto oposto {co} com o cateto adjacente {ca} resultam na hipotenusa {hip:.2f}')
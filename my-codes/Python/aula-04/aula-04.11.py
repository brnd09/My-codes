# DESAFIO 014 ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA DIGITADA EM °C E CONVERTA PARA °F

c = float(input('Escreva uma temperatura em graus célsius, °C: '))
f = c * 1.8 + 32
print(f'Sua temperatura em célsius é °C: {c:.2f}\nE sua temperatura em fahrenheit é °F: {f:.2f}')
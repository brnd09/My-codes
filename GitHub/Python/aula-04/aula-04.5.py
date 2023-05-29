# DESAFIO 008 ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO PARA CENTÍMETROS E MILÍMETROS 

n1 = float(input('Escreva um número em metros para que seja convertido para centímetros e milímetros: ' ))
cm = n1*100
mm = n1*1000
print('A medida de {}m  corresponde a, {}cm e {}mm '.format(n1, cm, mm))
# DESAFIO 015 ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE QUILÔMETROS PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO.
# CALCULE O PREÇO A PAGAR, SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0,15 POR QUILÔMETROS RODADO

dias_alugado = float(input('Por quantos dias você alugou o carro?: '))
km_percorrido = float(input('Quantos quilômetros seu carro percorreu?: '))                    
vl_d = dias_alugado * 60
vl_k = km_percorrido * 0.15
vl_t = vl_d + vl_k
print(f'O valor a se pagar pela diária é R${vl_d}, e o valor a se pagar pelo quilômetro rodado é R${vl_k}, logo o total a se pagar é R${vl_t}')
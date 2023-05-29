# DESAFIO 010 CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO A PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR CONSIDERE: US$:1,00 = R$:3,27

real = float(input('Quantos reais você tem na carteira? R$'))
cotação_do_dólar = 3.27
dólar = real / cotação_do_dólar
print('tendo R$:{:.2f} você consegue comprar US$:{:.2f}'.format(real, dólar))
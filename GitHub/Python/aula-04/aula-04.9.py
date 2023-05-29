# DESAFIO 012 FAÇA UM ALGORÍTIMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO

produto = float(input('Escreva o valor do produto: R$:')) 
desconto = produto * 0.05
preço_final = produto - desconto
print(' O valor original do produto é R${:.2f}\n O valor do desconto é de R${:.2f}\n O preço final é R${:.2f}'.format(produto, desconto, preço_final))
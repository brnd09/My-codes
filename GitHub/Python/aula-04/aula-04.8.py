# DESAFIO 011 FAÇA UM PROGRAMA QUE LEIA A ALTURA E A LARGURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTALA, 
# SABENDO QUE CADA LATA DE TINTA PINTA UMA ÁREA DE 2M QUADRADOS

altura = int(input('Qual é a altura da sua parede?: '))
largura = int(input('Qual é a largura da sua parde?: '))
área = int(altura * largura)
quantidade = int(área / 2)
print('a área da sua parede é de {}m², e a quantidade de latas de tinta necessárias para pintar sua parede serão {} latas'.format(área, quantidade))

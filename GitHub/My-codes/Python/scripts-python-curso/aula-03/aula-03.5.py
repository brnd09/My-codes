#DESAFIO 004 - FAZER UM PROGRAMA QUE LEIA ALGO E MOSTRE NA TELA SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELE

r  = input('Escreva alguma coisa:')
print('o tipo primitivo desse valor é-------------------:',type(r))
print('é alfabético?-------------------------------------:',r.isalpha())
print('é composto somente por caracteres maiúsculos?-----:',r.isupper())
print('é composto somente de caracteres minúsculas-------:',r.islower())
print('é alfa-numérico?:---------------------------------:',r.isalnum())
print('é composto somente por números?-------------------:',r.isnumeric())
print('é composto somente por decimais?------------------:',r.isdecimal())
print('é composto somente por dígitos?-------------------:',r.isdigit())
print('é composto somente por caracteres imprimÍveis?----:',r.isprintable())
print('esta dentro do padrão ASCII?----------------------:',r.isascii())
print('é válido em python?-------------------------------:',r.isidentifier())
print('é composto somente por espaços?-------------------:',r.isspace())
print('está em formato de título?------------------------:',r.istitle())
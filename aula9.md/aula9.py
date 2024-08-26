texto = 'bruno Leonardo  '

texto2= texto.capitalize()
# capitalize muda o primeiro caracter da string para maiusculo. Catalize precisa estar com () 
print (texto.capitalize())
print (texto2)


# lower padroniza a string em minusculo. Lower precisa estar com ()
### if nome ==nome1:
   # print('São iguais')
#else:
   # print('Não são iguais') 

nome = 'BrUNo lEoNaRDo'
nome1='bruno leonardo'
print(nome.lower())

if nome.lower() ==nome1.lower():
    print('São iguais')
else:
    print('Não são iguais')

# UPPER padroniza uma sring em maiusculas

print(nome.upper())

# replace muda um padrão de caracteres de uma string

mar = 'coração cabeção'
# mar2 = mar.replace('ç','c').replece('á','a')
# Ou mar2 =mar.replace('ã','a')
# Ou mar2 =mar.replace('ç','c')
print(mar.replace('çã', 'ca'))

#strip  remove caracteres em branco no final e no inicio de uma sting

jack= '      removendo o espaço       '

print(jack)
print(jack.strip())

# split pega cada letra e transforma em uma lista
#['Bruno', 'Leonardo'] - começa no zero, 1 e etc.
# print(string.split())
string= 'Bruno Leonardo'

print(string)
print(string.split())

# join transforma os elementos de uma lista em uma string, e consegue concatena uma string a outra

nome_lista= ['Bruno', 'Leonardo', 'Bonitão']
print(' '.join(nome_lista))

dominio = '@gmail.com'

print('bruno.leonardo' + dominio)

# slice manipula string por indice
cidade = 'Recanto das Emas, cidade do povo'
print(cidade [1:3])


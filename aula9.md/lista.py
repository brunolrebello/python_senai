# crud - create, read, update, delete - 
# create - insert;  reaad - select  - SQL

cavaleiros = ['Seya','Aldebaran','Aldebaran','Shun','Shiryu', 'Yoga']
print(cavaleiros)
#append adiciona um novo elemento ao final da lista
cavaleiros.append('Ikki')
print(cavaleiros)
# extend extedendo a lista com a outra lista
cavaleiros.extend(['Shina', 'Maryn'])
print(cavaleiros)
# insert inserir na lista em uma posição expecífica. O indice zero informa o pripeiro lugar. Mas poderia colocar em qualquer posição utilizando indice 1, 2, 3 e outros
cavaleiros.insert(0, 'Athena')
print(cavaleiros)

#remove, exclui um elemento pelo valor. Valor refere-se a informação, exemplo, os cavaleiros
cavaleiros.remove('Shun')
print(cavaleiros)
# pop exclui o último elemento da lista ou o indice informado. cavaleiros.pop()
elemento = cavaleiros.pop()
print(cavaleiros)
print(elemento)
# Passando a posição o pop exclui o informado, não passando ele exclui o último elemento
cavaleiros.pop(0)
print(cavaleiros)
#metodo indice(index) retorna o indice da primeira ocorrência de um valor procurado
print(cavaleiros.index('Yoga')) 

cavaleiros.pop(cavaleiros.index('Yoga'))
print(cavaleiros)

# alterando valor de um elemento da lista
cavaleiros[cavaleiros.index('Ikki')] = 'Ikki de Fenix'
print(cavaleiros)

# contabilizando quantidade de elementos repetidos
print(cavaleiros.count('Aldebaran'))
#sort ordenar de ordem crescente (Alfabetica ou númerica ou alfanumerico)
frutas = ['morango','maça','abacaxi','kiwi','amora','umbu', 'laranja', 'acerola', 'carambola']
numero = [2, 5, 80, 151, 4, 10, 74, 63, 52, 41, 22, 15, 30]

frutas.sort()
numero.sort()
print(frutas)
print(numero)

frutas.reverse()
print(frutas)
numero.reverse()
print(numero)
# para excluir o último elemento utiliza o -1.
del frutas[0]
print(frutas)

frutas.clear()
print(frutas)

# del frutas, como exemplo, exclui toda a lista, mandando para o limbo. Deixa de existir não podendo ser recuperado

del frutas
print(frutas)








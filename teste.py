frutas = ['acerola', 'maçã', 'uva', 'umbu']


def lista_frutas():
    for fruta in frutas:
        print(fruta)


def adicionar_fruta(nome):
    frutas.append(nome)


fruta = input('Qual a fruta deseja cadastrar?: ')
adicionar_fruta(fruta)
lista_frutas()

numeros=[
 [0,1,2],
 [3,4,5],
 [6,7,8]
]
for a, b, c in numeros:
   print(a,b,c)
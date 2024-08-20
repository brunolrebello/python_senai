# Curso de python no Senai

curso de capacitação de python ofertado pelo programa inovatech com Senai

|aula|descrição||
|-|-|-|
|01|introdução ao curso||
|02|introdução a linguagem markdown|[Aqui](./aulaMarkdown.md)
|03| compreendendo GIT|[Aqui](./aulaGit.md)
|cd code .| para abrir o aplicadivo
|int| para números inteiros
|float| para numeros quebrados
|String| para texto

n1 = 12
n2 = 7
# Operado maior quê
print(n1>n2)
print(n2>n1)
print(6 > 9)

# Operado menor quê

n3= 6
n4 = 3
print(n1<n2)
print(n2<n1)
---------------------------------------------------------------------
idade=int(input('Digite a sua idade: \n'))

if(idade > 120):
    print('Idade invalida')
elif(idade >= 18):
    print('Maior de idade')
elif(idade < 0):
    print('Ainda não nesceu')

else:
    print('Menor de idade')



---------------------------------------------------------
idade=int(input('Digite a sua idade: \n'))


if (idade>=18):
    print('Pode assistir ao filme')
elif(idade >= 16):
    acompanhado =input('Esta acompanhado de adulto "sim" ou "não" \n')
    if (acompanhado == 'sim'):
        print('Pode assistir ao filme')
    else:
       print('Não pode assistir ao filme')
else:
    print('Não pode assistir')
idade = int(input("informe a sua idade: \n"))
---------------------------------------------------------------------------
if(idade < 18):
    acompanhado = input('Está acompanhado de um adulto "sim" ou "não"? \n')
    if(acompanhado == 'sim'):
        print('Pode assistir')
    else:
        print('Não pode assistir')
else:
    print('Pode assistir')

    --------------------------------------------------------------------------
    aladdin = input('Aladdin apareceu? \n')
jasmine = input('Jasmin apareceu? \n')

if(aladdin == 'sim') and (jasmine == 'sim'):
    print('Love a noite inteira')
else: 
    print('Não teve encontro')
    =========================================================================
aladdin = input('Aladdin apareceu? \n')
jasmine = input('Jasmin apareceu? \n')

if(aladdin == 'sim') and (jasmine == 'sim'):
    print('Love a noite inteira')
else: 
    print('Não teve encontro')

if(aladdin == 'sim') or (jasmine =='sim'):
    print('Teve o seu encontro')
else:
    print('Não teve encontro')
    if not(aladdin == 'sim') or (jasmine =='sim'):
    print('Teve o seu encontro')
else:
    print('Não teve encontro')
-----------------------------------------------------------------

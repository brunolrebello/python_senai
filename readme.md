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

candidato = int(input('Informe o número do candidato: \n'))

if candidato == 13:
    print('Votou no molusco')
elif candidato == 22:
    print('Votou no louco')
else:
    print('Candidato invalido')

    candidato = int(input('Informe o número do candidato: \n'))


match candidato:
    case 13:
        print('Votou no molusco')
    case 22:
        print('Votou no doido')
    case _:
        print('Opção invalida')
---------------------------------------------------------------

if numero == 0:
    print('Número baixo')
elif numero ==1:
    print('Número baixo')
elif numero ==2:
    print('Número baixo')
elif numero==3:
    print('Número baixo')
elif numero==4:
    print('Número baixo')
elif numero ==5:
    print('Número média')
elif numero ==6:
    print('Número média')
elif numero ==7:
    print('Número média')
elif numero == 8:
    print('Número alta')
    -------------------------------------------------------
numero = 10
print(numero)

numero = numero + 10
print(numero)

numero = numero -10
print(numero)

numero *= 20
print(numero)

numero = numero /2
print(numero)


numero = 10
print(numero)

numero = numero + 10
print(numero)

numero = numero -10
print(numero)

numero *= 20
print(numero)

numero = numero /3

numero % 2 ==0
print('par')
numero % 1 == 1
print ('impar')
print(numero)

numero1 = int(input('Digite um número: \n'))

if numero1 % 2 == 0:

    print('Par')

else:
    print('Impar')

for i in range(5):
    print(i)
    ------------------------------------------------

    

frutas = ['maçã', 'morango', 'laranja','abacate']

for fruta in frutas:
   
    print(fruta[2])

for indice, fruta in enumerate(frutas):
    print(f'Suas fruta são {indice} - {fruta}')

    nomes = []

for i in range(5):
    nome = input('Informe o seu nome: \n')

nomes.append(nome)

for nome in nomes:
    print(nomes)

nome = 'Bruno'

for i in nome:
    print(i)

    -----------------------------------------------------------------------------
    numero = None
while numero != 0:
    numero = int(input('Digite um número \n'))
    ---------------------------------

    
nomes = []

for i in range(5):
    nome = input('Informe o seu nome: \n')

    nomes.append(nome)

for nome in nomes:
    print(nome)

nome = 'Bruno'

for i in nome:
    print(i)
    ---------------------------------------------------
    Crie um programa que pergunte ao usuário um número de 1 a 3 e exiba o nome correspondente ao número (1: "um", 2: "dois", 3: "três").
    2. Escreva um programa que peça ao usuário para inserir um número e verifique se o número é maior que 10.
    3. Desenvolva um programa que pergunte ao usuário o dia da semana (número de 1 a 7) e exiba o nome do dia correspondente.

4. Crie um algoritmo que solicite ao usuário uma cor (vermelho, verde, azul) e exiba uma mensagem correspondente à cor escolhida.

5. Faça um programa que solicite ao usuário dois números e verifique se ambos são pares.
6. Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) e dois números, e realize a operação escolhida.

7. Escreva um programa que peça ao usuário uma nota de 0 a 10 e classifique a nota como "Baixa", "Média" ou "Alta" usando match-case.

8. Desenvolva um algoritmo que pergunte ao usuário o estado civil (solteiro, casado, divorciado, viúvo) e exiba uma mensagem correspondente.

9. Crie um algoritmo que verifique se um número inserido pelo usuário é par ou ímpar.

10. Crie um algoritmo que solicite ao usuário uma idade e verifique se ela é maior ou igual a 18.

11. Escreva um programa que solicite ao usuário para digitar seu nome e, em seguida, exiba uma mensagem de boas-vindas personalizada.

12. Escreva um programa que peça ao usuário para escolher um modo de transporte (carro, bicicleta, a pé) e exiba uma mensagem com a velocidade média correspondente.

13. Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e exiba a estação do ano correspondente.

14. Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a soma deles é maior que 100.
-------------------------------------------------------------
number = 10
while True:
    number += 10
    if  number > 10000000:
        break
        -----------------------------------------------
15. Escreva um programa que pergunte ao usuário uma idade e verifique se a pessoa é adolescente (entre 13 e 19 anos).

16. Desenvolva um programa que peça ao usuário um tipo de combustível (gasolina, etanol, diesel) e exiba o preço correspondente por litro.

17. Crie um programa que solicite ao usuário dois números e exiba a soma, subtração, multiplicação e divisão entre eles.

18. Faça um programa que peça ao usuário três números e verifique se todos são positivos.

19. Escreva um algoritmo que peça ao usuário o nome de uma fruta e verifique se a fruta é uma maçã.

20. Crie um programa que solicite ao usuário a temperatura em graus Celsius e converta para Fahrenheit.

21. Escreva um algoritmo que peça ao usuário para digitar um número e verifique se ele é maior, menor ou igual a 10.

22. Escreva um programa que peça ao usuário para inserir dois números e verifique se o primeiro é maior que o segundo.

23. Crie um algoritmo que peça ao usuário uma palavra e verifique se a palavra é "Python".

24. Desenvolva um algoritmo que pergunte ao usuário o nome de uma cidade e verifique se é a capital do Brasil.

25. Escreva um programa que peça ao usuário um número de 0 a 20 e verifique se ele está entre 10 e 15.

26. Desenvolva um algoritmo que peça ao usuário para inserir dois números e verifique se ambos são múltiplos de 5.

27. Crie um programa que solicite ao usuário três números e exiba o maior deles.
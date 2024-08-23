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
28. Escreva um programa que peça ao usuário para inserir uma palavra e verifique se ela tem mais de 5 letras.

29. Crie um algoritmo que pergunte ao usuário um número e verifique se ele é múltiplo de 3.

30. Faça um programa que pergunte ao usuário a idade e verifique se ele pode votar (idade maior ou igual a 16).

31. Escreva um algoritmo que peça ao usuário um número de 1 a 5 e verifique se ele é igual a 3.

32. Escreva um programa que solicite ao usuário uma palavra e verifique se ela é uma palíndromo (lê-se igual de trás para frente).

33. Crie um programa que solicite ao usuário o valor de um produto e calcule o desconto de 10%.

34. Escreva um programa que peça ao usuário um número e verifique se ele é positivo, negativo ou zero.

35. Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a multiplicação deles é igual a 20.

36. Crie um programa que solicite ao usuário um número de 1 a 12 e exiba o mês correspondente.

37. Desenvolva um algoritmo que peça ao usuário para digitar um número e verifique se ele é múltiplo de 2 ou de 5.

38. Escreva um programa que peça ao usuário para digitar sua altura em metros e verifique se ela é maior que 1.75.

39. Crie um algoritmo que peça ao usuário para digitar uma senha e verifique se a senha é "1234".

40. Escreva um programa que peça ao usuário para inserir três números e verifique se todos são iguais.

41. Crie um programa que peça ao usuário um número inteiro positivo e exiba todos os números de 1 até o número informado.

42. Escreva um algoritmo que solicite ao usuário 5 números inteiros e calcule a soma desses números.

43. Desenvolva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e depois use um for para imprimir essa mensagem repetidas vezes.

44. Crie um programa que peça ao usuário 10 números e exiba apenas os números pares.

45. Escreva um algoritmo que peça ao usuário para inserir 5 números e, ao final, exiba o maior número inserido.

46. Desenvolva um programa que pergunte ao usuário para inserir 10 números e, ao final, exiba a média dos números inseridos.

47. Crie um programa que peça ao usuário um número e exiba a tabuada desse número de 1 a 10.

48. Escreva um algoritmo que solicite ao usuário uma palavra e exiba cada letra da palavra em uma linha separada.

49. Desenvolva um programa que peça ao usuário para inserir 7 números e, ao final, exiba quantos desses números são maiores que 10.

50. Crie um programa que peça ao usuário para inserir um número e, em seguida, exiba os números de 1 até esse número, mas de forma decrescente.

51. Crie um programa que peça ao usuário para inserir números até que ele digite o número 0. Ao final, exiba a soma de todos os números inseridos (exceto o 0).

52. Desenvolva um algoritmo que solicite ao usuário uma senha e continue pedindo até que a senha correta "1234" seja digitada.

53. Escreva um programa que peça ao usuário um número e exiba a contagem regressiva desse número até 1.

54. Crie um algoritmo que solicite ao usuário um número e continue pedindo outro número até que um número negativo seja inserido.

55. Desenvolva um programa que peça ao usuário para inserir um número maior que 100. Se o número for menor ou igual a 100, continue pedindo até que um número maior que 100 seja inserido.

56. Escreva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e utilize um laço while para exibir a mensagem a quantidade de vezes desejada.

57. Crie um programa que peça ao usuário para adivinhar um número secreto entre 1 e 10. Continue pedindo até que ele adivinhe o número corretamente.

58. Desenvolva um algoritmo que solicite ao usuário uma palavra e continue pedindo outra palavra até que ele digite "sair".

59. Escreva um programa que solicite ao usuário para digitar dois números e verifique se o primeiro é maior que o segundo. Continue pedindo números até que o primeiro número seja maior que o segundo.

60. Crie um programa que peça ao usuário um número e exiba todos os divisores desse número.

61. Crie uma lista contendo os números de 1 a 5 e imprima cada número da lista em uma linha separada.

62. Escreva um programa que solicite ao usuário para inserir 3 nomes e armazene-os em uma lista. Em seguida, imprima a lista completa.

63. Desenvolva um algoritmo que peça ao usuário para inserir 5 números, adicione-os a uma lista e, depois, exiba a soma de todos os números na lista.

64. Crie uma lista com 10 números aleatórios e exiba apenas os números que são múltiplos de 3.

65. Escreva um programa que solicite ao usuário uma lista de 5 números e exiba o maior e o menor número dessa lista.
#Desenvolva um algoritmo que peça ao usuário para inserir 5 números, adicione-os a uma lista e, 
# depois, exiba a soma de todos os números na lista.
numeros=[]


for i in range(5):
    numero = int(input(f'Digite o {i + 1}º número: '))
    

    numeros.append(numero)
    soma = sum(numeros)
    expressao = " + ".join(map(str, numeros))
print(f'O valor da soma dos números digitados: {expressao} =',soma)
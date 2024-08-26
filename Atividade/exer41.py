#Crie um programa que peça ao usuário um número inteiro positivo 
# e exiba todos os números de 1 até o número informado.
numero = int(input('Digite um número inteiro positivo: '))

if numero > 0:
    for i in range ( numero + 1):
        print(i)
else:
    print('O número digitado não é positivo. Tente outra vez. ')
    



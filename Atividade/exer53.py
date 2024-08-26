# Escreva um programa que peça ao usuário um número e exiba a contagem regressiva desse número até 1.

numero = int(input('Digite um número qualquer: '))

if numero >=0:
    for i in range(numero, 0, -1,):
        print(i)
        
elif numero <0:
    for i in range (numero, 0, 1):
        print(i)
    
else:
    print('Algo deu errado')
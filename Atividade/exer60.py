#Crie um programa que peça ao usuário um número e exiba todos os divisores desse número.
numero = int(input('Digite um número: '))

# Lista para armazenar os divisores
divisores = []

# Itera de 1 até o número para encontrar os divisores
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

# Exibe os divisores
print('Os divisores de', numero, 'são:', divisores)
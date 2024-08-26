# Desenvolva um programa que pergunte ao usuário para inserir 10 números e, ao final, 
# exiba a média dos números inseridos.
numeros=[]
for i in range(10):  
    numero = float(input(f'Insira o {i+1}º número: '))  # Pergunta ao usuário para inserir um número  
    numeros.append(numero)  # Adiciona o número à lista  

# Calcula a média  
media = sum(numeros) / len(numeros)  

# Exibe a média  
print(f'A média dos dez númmeros é: {media}')  
    
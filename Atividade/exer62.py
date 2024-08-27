#Escreva um programa que solicite ao usuário para inserir 3 nomes e armazene-os em uma lista. Em seguida, imprima a lista completa.

nomes=[]



for i in range(3):
    nome= input(f'Digite o {i+1}º nome: \n')
    nomes.append(nome)
    
print(f'O nomes inseridos são: {nomes}')
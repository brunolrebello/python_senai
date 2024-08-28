#Escreva um programa que solicite ao usuário uma lista de 
# 5 números e exiba o maior e o menor número dessa lista

numeros=[]

for i  in range(5):
    numero=int (input(f'Digite {i+1}º número: '))
    
    numeros.append(numero)
    
    maior_numero= max(numeros)
    minimo = min(numeros)
print(f'O valor minimo é: {minimo} e o maximo é {maior_numero}')


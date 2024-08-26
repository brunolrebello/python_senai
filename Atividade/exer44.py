#Crie um programa que peça ao usuário 10 números e exiba apenas os números pares.
numeros_pares=[]

for i in range(10):
    numero = int(input(f'Digite um números{i + 1}: '))
    if numero % 2==0:
     numeros_pares.append(numero)
   
if numeros_pares:
    print('Os números pares são esses:  ',numeros_pares)
else:
    print('Todos os números são ímpares')
        

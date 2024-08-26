 # Desenvolva um programa que peça ao usuário para inserir 7 números e, ao final, 
 #exiba quantos desses números são maiores que 10.
 
numeros_maior = []

for i in range (7):
    numero = int(input(f'Digite {i +1}º número: '))
    
    if numero > 10:
        numeros_maior.append(numero)
    
if numeros_maior:
      print(f'{len(numeros_maior)} Os números digitados são maiores que 10:', numeros_maior)
else:
    print('Os números digitados são menores que 10 ')

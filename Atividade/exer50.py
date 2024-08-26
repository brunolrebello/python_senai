#Crie um programa que peça ao usuário para inserir um número e, em seguida, 
# exiba os números de 1 até esse número, mas de forma decrescente.
numero = int(input('Digite um número qualquer: '))

if numero >=0:
    for i in range(numero, 0, -1,):
        print(i)
        
elif numero <0:
    for i in range (numero, 0, 1):
        print(i)
    
else:
    print('Algo deu errado')
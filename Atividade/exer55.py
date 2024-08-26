#Desenvolva um programa que peça ao usuário para inserir um número maior que 100. Se o número for 
# menor ou igual a 100, continue pedindo até que um número maior que 100 seja inserido.

while True:
    
    numero=int(input('Digite um número(ou número maior que 100 para parar): '))
    if numero > 100:
        break
    
           
print(f'A solicitação acabou')
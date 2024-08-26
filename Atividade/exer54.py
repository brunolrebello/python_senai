#Crie um algoritmo que solicite ao usuário um número e continue pedindo 
# outro número até que um número negativo seja inserido.

numero_negativo = []

while True:
    
    numero=int(input('Digite um número(ou número negativo para parar): '))
    if numero <=0:
        break
    
           
print(f'A solicitação acabou')
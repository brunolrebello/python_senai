#Crie um programa que peça ao usuário para adivinhar um número secreto entre 1 e 10. 
# Continue pedindo até que ele adivinhe o número corretamente.

numero_secreto= 3

while True:
    
    numero=int(input('Digite um numero entre 1 a 10: '))
    
    if numero ==numero_secreto:
       
     print(f'Você acertou o número secreto:{numero_secreto}')
    
    else:
     print('Continue tentando')
     break
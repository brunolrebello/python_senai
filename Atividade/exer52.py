#Desenvolva um algoritmo que solicite ao usuário uma senha e 
# continue pedindo até que a senha correta "1234" seja digitada.

while True:
    
    numero = int(input('Digite a senha: '))
    print('Tente novamente')
    if numero ==1234:
                break
print('Você acertou o a senha!!')
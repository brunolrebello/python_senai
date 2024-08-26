#Desenvolva um algoritmo que solicite ao usuário uma palavra 
# e continue pedindo outra palavra até que ele digite "sair".
dica = 'sair'

while True:
    
    palavra = str(input('Digite uma palavra(ou digite "sair" para parar)'))
    
    if palavra == dica:
        print('Você saiu do sistema')
        break
    else:
        print('Tente novament')
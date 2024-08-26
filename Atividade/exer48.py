# Escreva um algoritmo que solicite ao usuário uma palavra 
# e exiba cada letra da palavra em uma linha separada.
palavra = str(input('Digite uma palavra: '))

if palavra: 
    
    for letra in palavra:
        print(letra)
else:
    print('Nenhuma palavra foi digitada')


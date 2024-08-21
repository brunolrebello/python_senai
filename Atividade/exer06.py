numero = str(input('Escola uma opração mátematica: soma, subtração, multiplicação ou divisão. \n'))
numero1= int(input('Digite um numeros \n'))
numero2 = int(input('Digite o segundo número\n'))
soma, subt, mult, divi  = 0

if numero =='soma':
    soma = numero1 + numero2
    print('A soma é: ', soma)
elif numero =='subtração':
    subt = numero1 + numero2
    print('A subtração é: ', subt) 
elif numero == 'mult':
    mult = numero1 * numero2
    print('A multiplicação é: ', mult)
elif numero == 'divisão':
    divi= numero1 / numero2
    print('O resultado da divisão é: ', divi)        
else:
    print('Operação matematica invalida')       

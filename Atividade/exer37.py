numero = int(input('Digite um número: '))

if numero % 2==0:
    print('Número é multiplo de 2')
elif numero % 5 ==0:
    print('Número é multiplo de 5')
else:
    print('O número digitado não é multiplo de 2 ou de 5')
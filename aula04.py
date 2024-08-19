numero1= int(input('Digite o primeiro número \n'))
numero2= int(input('Digite o segundo número \n'))

soma = numero1 + numero2
subtraçao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print('O valor da soma é: ',soma)
print('O valor da subtração é: '+ str(subtraçao))
print('O valor da multiplicação é: {} e o valor da soma {} '.format(multiplicacao,soma))
print(f'O valor da divisão é: {divisao}')
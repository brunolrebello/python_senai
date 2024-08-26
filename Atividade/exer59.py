#Escreva um programa que solicite ao usuário para digitar dois números e verifique se o primeiro é maior que o segundo. 
# Continue pedindo números até que o primeiro número seja maior que o segundo.
while True:

 numero =int(input('Digite um número: '))
 numero1=int(input('Digite o segundo número: '))


 if numero>numero1:
        print('O primeiro número',numero, 'é maior que o segundo,',numero1)
    
        break
 else:
    print('Digite novamente')

    
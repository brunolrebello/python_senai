#Escreva um programa que solicite ao usuário uma palavra e verifique se ela é uma palíndromo (lê-se igual de trás para frente).

palindromo = 'Arara'

#if palindromo == palindromo[::-1]:
if palindromo.lower()== palindromo[::-1].lower():
    print('É palindromo')
else:
    print('Não é palindromo')





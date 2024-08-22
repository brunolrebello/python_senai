numero = int(input('Digite um número \n'))
numero1 = int(input('Digite o segundo numero \n'))
soma=0

soma = numero + numero1

if soma >100:
    print('A soma do ', numero,' e do ', numero1, ' o resultado é', soma,' é maior que 100')
elif soma >= 100:
    print('A soma do ', numero,' e do ', numero1,' o resultado é', soma,' é igual a 100')
else:
    print('A soma do ', numero,' e do ', numero1,' o resultado é', soma,' é menor que 100')
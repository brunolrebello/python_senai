numero = int(input('Digite um número qualquer: '))

if numero >=0:
    for i in range(0,numero + 1):
        print(i)
elif numero <1:
    for i in range (0,numero -1, -1):
        print(i)
else:
    print('Algo deu errado')

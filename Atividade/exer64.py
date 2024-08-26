lista=[]

for i in range(10):
    numero=int(input(f'Forneça {i+1}º número: '))
    if numero % 3 == 0:
        lista.append(numero)
for numero in lista:
    print('Os numeros são miltiplos de 3: ',numero) 
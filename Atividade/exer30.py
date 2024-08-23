# Arquivo respecivo ao ex07.py.
numero = int(input('Digite a sua idade \n'))

if 16 <= numero <= 17:
    print('O voto é opcional')
elif 18<= numero <=65:
    print('Você é obrigado a votar')
elif numero >65:
    print('Voto é opcional')
else:
    print('Você não vota')


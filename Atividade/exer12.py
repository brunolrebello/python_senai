nome = str(input('Escolha uma das opções de transporte: carro, bicicleta ou a pé \n'))

if nome == 'carro':
    print('A velocidade média do carro é de 100 km/h')
elif nome == 'bicicleta':
    print('A velocidade média da Bicicleta é de 25km/h')
elif nome == 'a pé':
    print('A velocidade média de andar a Pé é de 3,6km/h')
else:
    print('Opção invalida')


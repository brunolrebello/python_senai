nome = str(input('Digite o combustivel do seu automovel: gasolina, etanol ou diesel \n'))

if nome=='gasolina':
    print('O valor da gasolina hoje é de R$ 6,07')
elif nome == 'etanol':
    print('O valor da etanol hoje é de R$ 4,08')
elif nome == 'diesel':
    print('O valor da diesel hoje é de R$ 6,07')
else:
    print('A opção digita é invalida')
#  Escreva um algoritmo que forneça um menu para o usuário: 1-Cadastrar nome, 2- atualizar o nome, 3, excluir, 
# 4-listar todos os cadastrados, ao final da operação deve dar uma mensagem indicando o resultado da operação e perguntando se deseja realizar
# outra operação, o seu aplicativo apenas deve encerrar quando a opção não for inserida.

nomes=[]

operacao = 'sim'

while operacao =='sim':

    print('1-Cadastrar nome')
    print('2- atualizar o nome')
    print('3- excluir')
    print('4-listar todos os cadastrados')

    opcao = int(input('Informe a ação desejada: '))

    match opcao:
     case 1:
        print(opcao)
        nome = str(input('Digite o nome que desena cadastrar: '))
        nomes.append(nome)        
     case 2:
        nome = input('Qual nome deseja atualizar? ')
        novo_nome= input('Digite o novo nome: ')
        nomes[nomes.index(nome)] = novo_nome

     case 3:
        nome = input('Que nome deseja remover? ')
        nomes.remove(nome)

     case 4:
         for indece, nome in enumerate(nomes):
            print(f'{indece}, {nome}')
     case _:
        print('Opção invalida')

    operacao = input('Deseja realizar outra operação? \n').lower()

    if operacao != 'sim':
        break




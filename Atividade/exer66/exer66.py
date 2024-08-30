#  Escreva um algoritmo que forneça um menu para o usuário: 1-Cadastrar nome, 2- atualizar o nome, 3, excluir, 
# 4-listar todos os cadastrados, ao final da operação deve dar uma mensagem indicando o resultado da operação e perguntando se deseja realizar
# outra operação, o seu aplicativo apenas deve encerrar quando a opção não for inserida.
from os import system 


#from operacoes import menu, listar_nomes 
# inporte operacao

import operacoes as op



operacao = 'sim'


while operacao =='sim':

   op.menu()

   opcao = int(input('Informe a ação desejada: '))


   match opcao:
       case 1:
        print(opcao)
        nome = str(input('Digite o nome que deseja cadastrar: '))
        op.cadastrar_nome(nome)       

       case 2:

        nome = input('Qual nome que deseja atualizar? ')
        novo_nome= input('Digite o novo nome: ')
        op.atualiza_nome(nome,novo_nome)

       case 3:
        nome = input('Que nome deseja remover? ')
        op.excluir_nome(nome)

       case 4:
         op.listar_nomes()

       case _:
         print('Opção invalida')

   operacao = input('Deseja realizar outra operação? \n').lower()

   system('clear')

   if operacao != 'sim':
    break      




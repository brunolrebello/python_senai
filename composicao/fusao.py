from os import system

import projetos as pr

operacao ='sim'

while operacao.lower() == 'sim':
   
    pr.codigo()
    
    opcao = input("Informe a ação desejada: ")
    if opcao.isdigit():
        opcao=int(opcao)
    else:
      print('Entrada inválida! Por favor, insira um número válido.')
      
    
    match opcao:
        case 1:
          nome = input('Digite o nome do aluno: ')
          email = input('Digite o e-mail: ')
          nascimento = input('Digite a data de nascimento: ')
          pr.cadastrar_aluno(nome, email, nascimento)  
    
        case 2:
          matricula = int(input('Informe a matrícula do aluno a ser atualizado: '))
          novo_nome = input('Digite o novo nome (ou deixe em branco para não alterar): ')
          novo_email = input('Digite o novo e-mail (ou deixe em branco para não alterar): ')
          novo_nascimento = input('Digite a nova data de nascimento (ou deixe em branco para não alterar): ')
          pr.atualizar_dados(matricula, novo_nome or None, novo_email or None, novo_nascimento or None)

        case 3:
          matricula = int(input('Informe a matrícula do aluno a ser excluído: '))
          pr.excluir_aluno(matricula)

        case 4:
           pr.listar_alunos()
        case 5:
          print('Programa encerrado.')
          break
        
        case _:
            print('Opção inválida.')
            
    operacao = input('Deseja realizar outra operação? (sim/não): ').lower()
    pr.os.system('cls' if pr.os.name == 'nt' else 'clear')        
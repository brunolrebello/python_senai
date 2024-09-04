
nomes = []
matricula= 1

def menu():

  opcoes = ['Cadastrar nome','atualizar o nome', 'excluir', 'listar todos os cadastrados']

  for indice, opcao in enumerate(opcoes):
    print(f'{indice+1} - {opcao}')

def listar_nomes():

   for indice, nome in enumerate(nomes):
      print(f'{indice} - {nome}')

def cadastrar_nome(nome, email, data_nascimento, matricula):
    
    aluno = {
        'nome': nome,
        'e-mail':email,
        'data_nascimento':data_nascimento,
        'matricula':matricula
         
    }
    nomes.append(aluno)


def atualiza_nome(nome,novo_nome):
    nomes[nomes.index(nome)] = novo_nome

def excluir_nome(nome):
    nomes.remove(nome)



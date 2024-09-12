
nomes=[]
matriculas=[]
emails=[]
data_nascimento = []

def codplay():
    tipagem = ['Matricula','Cadastrar nome','e-mail', 'data de nascimento', 'Atualizar nome', 'Excluir', 'Listar todos os cadastros' ]
    for indice, tipagens in enumerate (tipagem):
        print(f'{indice + 1} - {tipagens}')
        
def lista_nomes():
    for indice, nome, matricula, email, nascimento in enumerate(nomes, matriculas, emails, data_nascimento):
        print(f'{indice} - {matricula} - {nome} - {email} - {nascimento}')

def cadastrar_matricula(matricula):
    matriculas.append(matricula)
    
def cadastrar_email(email):
     emails.append(email)
def cadastrar_data_nascimento(nascimento):
   data_nascimento.append(nascimento)
def cadastrar_nome(nome):
    nomes.append(nome)   

def atualizar_nome(nome,novo_nome):
    nomes[nomes.index(nome)] = novo_nome     

def atualizar_email(email, novo_email):
    emails[emails.index(email)] = novo_email
    
def atualizar_nascimento(nascimento, novo_nascimento):
    data_nascimento[data_nascimento.index(nascimento)] = novo_nascimento 
      
def excluir_nome(nome):
    index = nomes.index(nome)
    nomes.pop(index)
    emails.pop(index)
    data_nascimento.pop(index)
          







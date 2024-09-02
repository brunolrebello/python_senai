import os

base_dados={}
nomes=[]

proxima_matriculas= 1    

emails=[]
data_nascimento=[]


def gerar_matricula():
    global proxima_matriculas
    matricula = proxima_matriculas
    proxima_matriculas += 1
    return matricula

def cadastrar_aluno(nome, email, nascimento):
    matricula = gerar_matricula()
    base_dados[matricula]={
        'nome':nome,
        'email': email,
        'nascimento': nascimento   
        
    }
    print(f'Aluno cadastrado com sucesso! Matricula: {matricula}')
    
def listar_alunos():
    if not base_dados:
        print('Nehum aluno cadastrado.')    
    else: 
        for  matricula, dados in base_dados.items():
            print(f'Matrícula: {matricula} - Nome: {dados['nome']} - Email: {dados['email']} - Data de Nascimento: {dados['nascimento']}')    
    
def excluir_aluno(matricula):
    if matricula in base_dados:
         del base_dados[matricula]
         print(f'Aluno com matrícula  {matricula} não enconttrada')    
def atualizar_dados(matricula, novo_nome=None, novo_email=None, novo_nascimento=None):  
    if matricula in base_dados:
        if novo_nome:
            base_dados[matricula]['nome']= novo_nome
        if novo_email:
            base_dados[matricula]['email']=novo_email
        if novo_nascimento:
            base_dados[matricula]['nascimento'] = novo_nascimento
        print(f'Dados do Aluno com matrícula {matricula} - atualizada com sucesso!! ')
    else:
        print(f'Matrícula não encontrada.')
def codigo():
    print("1 - Cadastrar Aluno")
    print("2 - Atualizar Dados de Aluno")
    print("3 - Excluir Aluno")
    print("4 - Listar Todos os Alunos")
    print("5 - Sair")
    
    
    
    
    
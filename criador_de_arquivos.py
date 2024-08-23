import os

def criar_arquivos_py(caminho_pasta, quantidade_arquivos):
    # Verifica se o diretório existe, caso contrário, cria-o
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

    for i in range(1, quantidade_arquivos + 1):
        nome_arquivo = f"exer{i:02}.py"  # Formato ex01.py, ex02.py, etc.
        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

        # Verifica se o arquivo já existe, incrementando o número até encontrar um disponível
        while os.path.exists(caminho_arquivo):
            i += 1
            nome_arquivo = f"exer{i:02}.py"
            caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

        # Cria o arquivo
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write(f"# Arquivo respecivo ao {nome_arquivo}.\n")

        print(f"Arquivo criado: {caminho_arquivo}")

quantidade_arquivos = int(input('Quantidade de arquivos: '))
caminho = input("digite o diretório que os arquivos serão criados: ")  # Diretório onde os arquivos serão criados

nome_arquivo = None
quantidade = quantidade_arquivos  # Número de arquivos que deseja criar
criar_arquivos_py(caminho, quantidade)


quantidade = int(input("Digite a quantidade de arquivos .py que deseja criar: "))

for i in range(1, quantidade + 1):
    Atividade = f"arquivo_{i}.py"
with open(Atividade, 'w') as arquivo:
         arquivo.write(f"# Este é o arquivo {Atividade}\n")
print(f"{Atividade} foi criado com sucesso!")
print("Todos os arquivos foram criados.")
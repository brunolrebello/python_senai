numero = [1, 5, 60, 3, 100, 202, 7, 150, 5, 200, 4]
numero1= 3
numero2 = 5
print(max(numero))
print(min(numero))
print(len(numero))
print(sum(numero))

media = sum(numero)/ len(numero)
print(media)

def media(numero):
   resultado =  sum(numero) / len(numero)
   return resultado

media(numero)
print(media(numero))

# função recebe dois numeros e soma
# O nome da variável pode ser qualquer um. Tanto que na média está um nome na soma outro parametro.
def soma(a , b, e, f,g):
    soma = a + b+ e+ g

    return soma

print(soma(numero1, numero2, 50, 14,36))

print(soma(50, 30, 45, 36, 15))
print(soma(numero1 , numero2, 2, 3, 100))

# Lambda é resumir uma função.
somar = lambda a, b: a + b 
print (somar(35, 15))


# função de subtração
def sub(c,d):
    sub = c - d
    return sub

print(sub(265, 165))
print(sub(numero1, numero2))

# Uso da função sem o uso do return (retorno)

def saudacao(nome):
    print(f'Olá! {nome}, Seja bem vindo!!')
saudacao('Bruno')

#função opcional se o usuario não colocar ele aparece Exemplo: mensagem="olá", vai aparecer o que for colocado.

def ola(nome, mensagem = 'Olá'):
    print(mensagem, nome)

ola('Bruno Leonardo', 'Tudo bem?')


# função de multiplo retorno
# para ter o valor absoluto, o numero inteiro sem numeros após a virgula
def dividir(a , b):
    resposta = a // b
# Esse calculo é para saber os números após a virgula, o que seria o resto
    resto = a % b
# O return pode ter varios retornos, desde que separados por virgula. exemplo abaixo
    return resposta, resto


divisao, resto_divisao = dividir(9,2)
print(divisao)
print(resto_divisao)


digo, viro= dividir(10, 2)
print(digo)

# Tuple é imutavél. Não se mexe de forma alguma. Caso precise deve ir até a variavel para modificar, caso contrario não é possível

numeros = (4, 5, 6, 8, 10, 11, 12) # é preciso estar em [], caso contrario vai dar o erro.
print(type(numeros)) 


# paramentro não nomeado conhecido posicional. Quando manda apenas o valor sem especificar nada
# quando manda varios parametros chama-se argumentos
# o asterisco é que pode ser colocado infinitos argumentos. O nome pode ser qualquer um, mas este exemplo foi utilizado "args" de argumento
def exibir_infor(*args):
    print('Argumentos posicionais',args)

exibir_infor(1, 4, 'Bruno', 'Case', 45, 'valido', 10)

#com dois asterisco precisa dizer o nome
#  paramentro ou argumento nomeado quando aparece em chave. 
# Dicionario 
def exibir_infor2(**args):

    print('Argumentos nomeados',args)

exibir_infor2(soma = 30 + 10 +30 , Nome=  'Bruno', curso='Python')

# chave e do lado direito valor. Exemplo  nome: bruno - key: value  chave : valor
# tudo que está entre chave é chamado dicionário
# os colchetes representa uma lista. Neste exemplo pode ter um dicionario em uma lista

pessoa= [{ 
    'nome':'Bruno Leonardo', 
    'idade': 35, 
    'estado_civil': 'casado', 
    'escolaridade': 
    'superior completo'
},

{ 
    'nome':'Marianna', 
    'idade': 38, 
    'estado_civil': 'casado', 
    'escolaridade': 'superior completo'
}]

print(pessoa [0])

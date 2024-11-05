#Crie uma lista chamada ‘usuarios’ que contenha ao menos 5 listas. Cada lista interna deve representar um usuário do INFwebNET com as seguintes informações: nome (string), idade (inteiro), cidade (string) e estado (string).
import random as rd

print("Exercicio 1")
'''Criado a lista usuário e feito um aninhado de listas.'''
usuarios = [
    ["Kaio", 23, "Caruaru", "PE"],
    ["Pedro", 20, "Recife", "PE"],
    ["Diego", 30, "Caruaru", "PE"],
    ["Carlos", 24, "Uberaba", "MG"],
    ["Eduardo", 26, "João Pessoa", "PB"]
]
print(usuarios)
#Escreva um programa que leia os dados da lista ‘usuarios’ criada no exercício anterior e crie um dicionário para cada usuário. Cada dicionário deve ter as chaves "nome" e "idade" com os respectivos valores, e a chave "localização" contendo uma tupla (cidade, estado). Armazene esses dicionários em uma nova lista chamada perfis.
print("Exercicio 2")
perfis = []
'''Loop para interação percorrendo todo o dicionário e adicionando os respectivos valores. Criado a tupla para a adicionar valores chaves : valor'''
for usuario in usuarios:
    
    dicionario = {
        "nome" : usuario[0],
        "idade" : usuario[1],
        "localização" : {
            "cidade" : usuario[2],
            "estado" : usuario[3]
        }
    }
    
    perfis.append(dicionario)
print(perfis)

#Explique, em poucas palavras, as principais diferenças entre uma lista, um dicionário e uma tupla em Python. Dê exemplos de como cada estrutura pode ser usada no contexto da análise de dados do INFwebNET.Explique, em poucas palavras, as principais diferenças entre uma lista, um dicionário e uma tupla em Python. Dê exemplos de como cada estrutura pode ser usada no contexto da análise de dados do INFwebNET.
print("Exercicio 3")
print("Está em Docstring")
'''Resposta: Listas: Podem ter valores duplicados, são mutaveis(Alteraveis: adicionar, excluir, atualizar)
             Dicionários: Não podem ter valores duplicados,são usado por valores pares "Chaves : Valor", são mutaveis(Alterações: adicionar, excluir, atualizar.)
             Tuplas: Podem ter valores duplicados, são imutaveis(Ao criar uma tupla, não podemos adicionar, excluir e nem atualizar-las). '''
             
#Alguns usuários do INFwebNET forneceram informações incompletas. Remova da lista perfis todos os perfis que não possuem as informações de "nome" ou "cidade". Mantenha a lista perfis original intacta, criando uma nova lista chamada perfis_validos para armazenar os perfis válidos.
print("Exercicio 4")

perfis_validos = [
    perfil for perfil in perfis
    if "nome" in perfil and perfil["nome"] and 
       "localização" in perfil and perfil["localização"]["cidade"]
]
print(perfis_validos)

#Crie uma implementação que leia os dados presentes no arquivo "base_inicial.txt" e os armazene na lista perfis_validos, criando novas palavras-chave para os dados adicionais encontrados. (O arquivo está disponível no repositório.)
print("Exercicio 5")
'''Abrindo o arquivo .txt para a manipulação de dados, criado uma estrutura para tratamento de dados. Para fins de redundancia no codigo. Usado o strip e o split para tal tratamento. '''
perfis_validos = []

with open("./Python_Dados_TP1/base_inicial.txt", mode="r", encoding='utf-8') as texto:
    content = texto.readlines()

for linha in content:
    linha = linha.strip()
    if not linha:
        continue

    dados = linha.split('?')
    
    print(f"Processando linha: {dados} (Total de elementos: {len(dados)})")
    
    if len(dados) >= 5:
        perfil = {
            "nome": dados[0],
            "idade": dados[1],
            "localização": {
                "cidade": dados[2],
                "estado": dados[3]
            },
            "amigos": set(dados[4:])  # Junta os elementos restantes como amigos
        }
        perfis_validos.append(perfil)

print("\nPerfis Válidos:")
for perfil in perfis_validos:
    print(f"Nome: {perfil['nome']}")
    print(f"Idade: {perfil['idade']}")
    print(f"Cidade: {perfil['localização']['cidade']}")
    print(f"Estado: {perfil['localização']['estado']}")
    print(f"Amigos: {', '.join(perfil['amigos'])}")  # Junta os amigos em uma string
    print("-" * 40)

#Com os dados carregados no exercício anterior, adicione os usuários dos exercícios 1 e 2, definindo um padrão para lidar com os dados ausentes e salve estas informações em um arquivo "rede_INFNET.txt".
print("Exercicio 6")

perfis = []
for usuario in perfis_validos:
    dicionario = {
        "nome": usuario["nome"],
        "idade": usuario["idade"],
        "localização": {
            "cidade": usuario["localização"]["cidade"],
            "estado": usuario["localização"]["estado"]
        },
        "amigos": usuario["amigos"]
    }
    perfis.append(dicionario)

with open("rede_INFNET.txt", mode="w", encoding='utf-8') as f:
    for perfil in perfis:
        f.write(f"{perfil['nome']}?{perfil['idade']}?{perfil['localização']['cidade']}?{perfil['localização']['estado']}?{perfil['amigos']}\n")

print("Dados salvos em rede_INFNET.txt.")
#Com o dicionário criado no exercício anterior, adicione um novo amigo ao set de amigos de um usuário específico.
print("Exercicio 7")
print("-" * 40)
perfis[5]["amigos"].add("Lucivania")
print("Usuário com a lista de amigos atualizadas.")

print(f"Nome: {perfis[5]['nome']}")
print(f"Idade: {perfis[5]['idade']}")
print(f"Cidade: {perfis[5]['localização']['cidade']}")
print(f"Estado: {perfis[5]['localização']['estado']}")
print(f"Amigos: {', '.join(perfis[5]['amigos'])}")
print("-" * 40)

#Crie um programa que permita verificar se um determinado usuário foi adicionado como amigo de mais de 4 usuários. Caso tenha, exiba uma mensagem afirmando que o usuário é "popular".
print("Exercicio 8")

usuarios_populares = {}
for usuario in perfis:
    for nome in usuario['amigos']:
        if nome in usuarios_populares:
            usuarios_populares[nome] += 1
        else:
            usuarios_populares.update({nome: 1})

lista_populares = usuarios_populares.keys()

for usuario in lista_populares:
    if usuarios_populares[usuario] >= 4:
        print(f"Usuário: {usuario} é popular!")
print("-" * 40)

#Crie um programa que selecione dois perfis aleatórios e utilize sets para armazenar os amigos de cada um desses usuários do INFwebNET. Exiba os amigos em comum entre esses dois usuários, utilizando métodos e operação de sets.
print("Exercicio 9")

lista_usuarios = list(usuarios_populares.keys())
usuario_aleatorio1 = rd.choice(lista_usuarios)
usuario_aleatorio2 = rd.choice(lista_usuarios)

amigos_comum = set()
amigos_usuario1 = set()
amigos_usuario2 = set()

for usuario in perfis:
    if usuario['nome'] == usuario_aleatorio1:
        amigos_usuario1 = usuario['amigos']
    elif usuario['nome'] == usuario_aleatorio2:
        amigos_usuario2 = usuario['amigos']
    
for amigo in amigos_usuario1:
    if amigo in amigos_usuario2:
        amigos_comum.add(amigo)
        
if len(amigos_comum) == 0:
    print(f"Usuários: {usuario_aleatorio1} e o {usuario_aleatorio2} não possuem amigos em comum.")
else:
    print(f"Usuários: {usuario_aleatorio1} e o {usuario_aleatorio2} possuem esses amigos em comum.")
    for amigo in amigos_comum:
        print(amigo)
print("-" * 40)        

#Utilizando os sets do exercício anterior, exiba os amigos que são exclusivos de cada usuário, ou seja, aqueles que não são amigos em comum.
print("Exercicio 10")

amigos_diferentes = set()

for amigo in amigos_usuario1:
    if amigo not in amigos_usuario2:
        amigos_diferentes.add(amigo)
        
if len(amigos_diferentes) == 0:
    print(f"Usuários: {usuario_aleatorio1} e o {usuario_aleatorio2} não possuem amigos diferentes.")
else:
    print(f"Usuários: {usuario_aleatorio1} e o {usuario_aleatorio2} possuem esses amigos diferentes.")
    for amigo in amigos_diferentes:
        print(amigo)
print("-" * 40)        

#Permita que o usuário remova um amigo da lista de conexões de um membro do INFwebNET específico no dicionário criado no exercício 4.
print("Exercicio 11")

with open("./Python_Dados_TP1/rede_INFNET.txt", mode='r', encoding='utf-8') as file:
    content = file.readlines()
    
print(content)

for usuario in perfis:
    
    
#Após adicionar ou remover amigos, salve o dicionário atualizado em um novo arquivo chamado "rede_INFNET_atualizado.txt".
    print("Exercicio 12")

#Escreva um programa que leia o arquivo "rede_INFNET.txt" e imprima na tela a lista dos nomes de todos os usuários da rede social.
print("Exercicio 13")
with open('./rede_INFNET.txt', mode='r', encoding='utf-8') as file:
    content = file.readlines()
    
    content = content.replace("{", "").replace("}", " ").replace("'", "?")
    
    print(content)
    
#Crie uma função que leia o arquivo "rede_INFNET.txt" e mostre quantos amigos cada usuário possui, imprimindo o nome do usuário e a quantidade de amigos.
print("Exercicio 14")

#Analise o arquivo "rede_INFNET_atualizado.txt" e identifique os 5 usuários que foram marcados como amigos pelo maior número de usuários cadastrados. Exiba o nome desses usuários e a quantidade de amigos que cada um possui.
print("Exercicio 15")

#Explique com suas palavras a importância de utilizar o recurso ‘with’ ao lidar com arquivos em Python.
print("Exercicio 16")

'''A importancia do uso do With são várias, algumas delas é simplesmente pelo fato de ao usar o with, o programa le o arquivo e logo em seguida o fecha rapidamente e também preserva o arquivo para não haver dados corrompidos pelo fato de que o arquivo sempre está aberto. Além disso o uso do with é uma forma mais concisa e mais limpa(Menos verboso) fazendo com que fique mais simples a identificação e a leitura do codigo para uma futura fatoração. E por fim, existe um melhor gerenciamento de recursos ou seja, ao usar o with evitamos o vazamento de recursos. Ou seja, podemos economizar recursos do hardware que está sendo usado para manter o arquivo aberto.'''

'''Desculpe por não finalizar todas as questões por motivos de trabalhos resultou em pouco tempo para a resolução de questões e queria enviar todas. Porém não quero enviar atrasada para o meu AT não ficar na nota minima. Irei organizar melhor meu tempo para não ocorrer novamente este problema. Desde já peço desculpas novamente.(Final de ano aqui onde trabalho o serviço sempre é triplicado). Luiz creio que conhece a Feira de Caruaru e trabalho por lá. Final de ano é muito trabalho... Desde já, sei que não muda o fato de que não cumpri 100% dos meus deveres como aluno.'''
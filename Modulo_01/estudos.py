#nome_completo = input(str("Digite seu nome: "))

#print(f"Olá {nome_completo}, tudo bem? Seja bem vindo! Qual seu desejo?")

#print(nome_completo.count("a"))
 
#count conta a quantidade de determinada string em especifico e o find mostra a posição. (lembrando que se inicia no 0)
#encode transforma em byte codifica e o decode decodifica para um tipo texto comum
#replace substitui, gosto muito desse!
#print("-".join(nome_completo)) #vai dividir com - o nome, ex: g-i-a-n
#.split divide uma variavel e gera liste com base nas mesmas separadas
#.strip("x") vai remover o que fica no inicio ou no fim de um caractere exemplo: vai ser eliminado o x
#.startswith("") da true ou false dependendo da condição que vc coloca
#in compara na variavel se existe ex "gi" in nome_completo - se tiver vai sair true (TAMBEM EXISTE NOT IN )

#-----------------------------------------------------------------------------------------------------------
#LISTAS SÃO COLEÇÕES ORDENADAS E MUTAVEIS

#lista = [1, 3,nome_completo,4,"oieee"]

#print(lista[4:8]) #fatia a lista

#meteodo append(): adiciona um elemento no final da lista

#.index() mostra a posição do elemento na lista

#.insert( , ) funciona como um replace dentro da lista

#.pop() remove um elemento com base na posição

#.remove() remove um elemento com valor específicado

#.sort() organiza a lista em ordem crescente, mas não suporta int e str juntos 



#----------------------------------------------------------------------------------------------------------

#TUPLAS SÃO COLEÇÕES ORDENADAS E IMÚTAVEIS != LISTA
#minha_tupla = (1,2,2,3,4)
#print(minha_tupla)

#Método Count conta quantas vezes um elemento se repete na tupla

#contagem = minha_tupla.count(2)
#print(contagem)

#método INDEX mostra a posição do elemento na tupla

#indice = minha_tupla.index(3)
#print(indice)

#--------------------------------------------------------------------------------------------------------------
#dicionários são coleções não ordenadas onde a estrutura pressupõe uma "chave": valor

######del pessoa["sobrenome"]

#Métodos: keys() mostra as chaves dos dicionários (se quiser uma chave específica transformar em lista)-
#  values() retorno dos valores dentro das chaves (tambem transformar em lista se desejar um valor específico)-
#  items() mostra todas as chaves-valor em formato de tupla (tambem transformado em lista se for necessário valor específico mas com duas [][] para um valor)

# -------------------------------------------------------------------------------------------------------------

#CONDICIONAIS IF , ELIF e ELSE
# print("SEJA BEM-VINDO AO BARZINHO!!!!")
# idade =int(input("Digite sua idade: \n"))

# if idade >= 18:
#     print("Você é de maior")

# elif idade > 13:
#     print("Você é adolescente")

# else: 
#     print(f"{idade} anos?? Rala Pirralho!")

# ---------------------------------------------------------------------------------------------------------

#FOR 
# lista = [1,2,3,4,5]
# for elemento in lista:
#     print(elemento)

# tupla = (1,2,3,4,5)
# for elemento in tupla:
#     print(elemento)

# pessoa = {"nome": "Gianlucca", "Sobrenome": "Boghi", "Idade": 23 }
# print("\t FOR UTILIZANDO DICIONARIO - CHAVES")
# for chave in pessoa.keys():
#     print(chave)
# print("\n \t FOR UTILIZANDO DICIONARIO - VALORES")
# for valor in pessoa.values():
#     print(valor)
# print("\n \t FOR UTILIZANDO DICIONARIO - ITENS")
# for itens in pessoa.items():
#     print(itens)

# #Range(): intervalo numerico
# # "[0,1,2,3,4,5,6,7,8,9]" = range(0,10)  - Pode ser convertido para lista
# for numero in range(5):
#     print("Numero: ", numero)


# lista = [1,2,3,4,5]
# print(lista)
# for indice in range(0, len(lista)):
#     if indice ==3:
#         lista[indice] = 5
#     else:
#         lista[indice]=0
# print(lista)

# #enumerate() - Permite que você saiba o indice e o valor de uma lista (da pra substituir o range e o len)
# for indice, valor in enumerate(lista):
#     print(f"{indice} , {valor}")

#---------------------------------------------------------------------------------------------------------------------------

#WHILE - LOOPING DE REPETIR ENQUANTO UMA CONDIÇÃO FOR VERDADEIRA

# contador = 0
# while contador <=5:
#     print("Contagem: ", contador)
#     contador +=1

# print("Programa finalizado")

#----------------------------------------------------------------------------------------------------------------------------
#FUNÇÕES
#REALIZA TAREFAS ESPECÍFICAS NO CÓDIGO
#EXEMPLO

def saudacao(nome):
    print(f"Ola, {nome}!")

print("Chamando a função saudacao: ")
saudacao("Alice")
saudacao("Bob")

# função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("Chamando função quadrado: ")
resultado_quadrado = quadrado(int(input("Digite o número: ")))
print(resultado_quadrado)

#função com multiplos parametros
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("Chamando a função soma: ")
resultado_soma = soma(20,50)
print("A soma do numero 20 e numero 50 é", resultado_soma )
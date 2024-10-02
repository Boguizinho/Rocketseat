#Linguagem de programação orientada a objetos
#Permite que os programadores criem softwares modulares e reutilizaveis 
#Organização de programas em volta de objetos

# # Classe exemplo
# class Pessoa:
#     def __init__(self,nome, idade) -> None:             #def fora de uma classe é uma função e dentro é um método
#         self.nome = nome
#         self.idade = idade

#     def saudacao(self):
#         return f"Ola, meu nome eh {self.nome} e eu tenho {self.idade} anos."

# #Objeto - criado a partir de uma classe
# pessoa1 = Pessoa("Alice",30)
# mensagem = pessoa1.saudacao()
# print(mensagem)

# pessoa2= Pessoa("Rodrigo", 22)
# # mensagem = pessoa2.saudacao()
# # print(mensagem)

# #Uma das principais utilizações de Classe e Objeto é a reutilização de códigos


# #-----------------------------------------------------------------------------------------------------------------
# # PILARES DE PROGRAMAÇÃO ORIENTADA AO OBJETO  (Serve para todas as linguagens)
# # 1- HERANÇA 
# # 
# # Exemplo de herança
# print("\nExemplo de herança: ")
# class Animal:
#     def __init__(self, nome) -> None:
#         self.nome = nome

#     def andar(self):
#         print(f"O animal {self.nome} andou")
#         return
    
#     def emitir_som(self):
#         pass

# class Cachorro(Animal):
#     def emitir_som(self):
#         return "AU AU"
    

# class Gato(Animal):
#     def emitir_som(self):
#         return "Miau"
    
# # Herança é quando uma classe reaproveita a estrutura de uma classe anterior ou a classe em si
# dog = Cachorro(nome="Rex")
# cat = Gato(nome="Felix")

# # 2- POLIMORFISMO
# #  O Polimorfismo acontece quando duas classes diferentes utilizam um mesmo método mas com valores diferentes, como o cachorro e o gato
# #  que ambos possuem o "emitir_som" mas cada um tem seu valor diferente
# print("\nExemplo de polimorfismo")
# animais = [dog, cat]

# for animal in animais:
#     print(f"{animal.nome} faz: {animal.emitir_som()}")

# # 3- ENCAPSULAMENTO
# # São dados secretos que não são acessáveis exceto dentro dos métodos
# print("\nExemplo de encapsulamento: ")
# class ContaBancaria:
#     def __init__(self, saldo) -> None:
#         self.__saldo = saldo #atributo privado quando você coloca 2x "_"

#     def depositar(self, valor):
#         if valor > 0:
#             self.__saldo += valor

#     def sacar(self,valor):
#         if valor > 0  and valor <= self.__saldo:
#             self.__saldo -= valor

#     def consultar_saldo(self):
#         return self.__saldo

# conta = ContaBancaria(saldo=1000)
# print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
# conta.depositar(valor=500)
# print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
# conta.depositar(valor=-500)
# print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
# conta.sacar(valor=200)
# print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

# conta_do_zezinho = ContaBancaria(saldo=50)

# # 4- ABSTRAÇÃO 
# # Define necessária uma implementação de um método, deixa ele obrigatório a ser utilizado
# print("\nExemplo de Abstração: ")
# from abc import ABC, abstractmethod

# class Veiculo(ABC):

#     @abstractmethod
#     def ligar(self):
#         pass

#     @abstractmethod
#     def desligar(self):
#         pass

# class Carro(Veiculo):
#     def __init__(self) -> None:
#         pass


#     def ligar(self):
#         return "Carro ligado usando a chave"
    
#     def desligar(self):
#         return "Carro Desligado"
    

# carro_amarelo = Carro()

# print(carro_amarelo.ligar())
# print(carro_amarelo.desligar())

#--------------------------------------------------------------------------------------------------

# HERANÇA MÚLTIPLA

# class Animal:
#     def __init__(self, nome) -> None:
#         self.nome = nome 

#     def emitir_som(self):
#         pass

# class Mamifero(Animal):
#     def amamentar(self):
#         return f"{self.nome} esta amamentando!"
    
# class Ave(Animal):
#     def voar(self):
#         return f"{self.nome} está voando!"
    
# class Morcego(Mamifero, Ave):           #Herança multipla, pois um morcego é uma ave e um mamífero
#     def emitir_som(self):
#         return "Morcegos emitem sons ultrassônicos"
    
# morcego = Morcego(nome= "Batman")

# #Acessando métodos da classe base "Animal"

# print("Nome do morcego:", morcego.nome)
# print(f"Som do morcego: {morcego.emitir_som()}")

# #Acessando métodos das classes 'Mamífero' e 'Ave'
# print("Morcego amamentando:", morcego.amamentar())
# print("Morcego voando:", morcego.voar())

#-------------------------------------------------------------------------------------------------------------------------------

# DECORADORES
# tipo de função que permite modificar ou extender o comportamento de outras funções/métodos sem alterar o código original

# from typing import Any


# def meu_decorador(func):
#     def wrapper():
#         print("Antes da minha função ser chamada")
#         func()
#         print("Depois da minha função ser chamada")
#     return wrapper

# @meu_decorador  #Chama o seu decorador  
# def minha_funcao():
#     print("Minha função foi chamada")

# minha_funcao()

# class MeuDecoradorDeClasse:
#     def __init__(self, func) -> None:
#         self.func = func

#     def __call__(self) -> Any:
#         print("Antes da funcção ser chamada (decorador de classe)")
#         self.func()
#         print("Depois da função ser chamada")

# @MeuDecoradorDeClasse
# def segunda_funcao():
#     print("Segunda função foi chamada")

# segunda_funcao()


#------------------------------------------------------------------------------------------------------------------
#DECORADORES COMUNS:
#@classmethod
#@staticmethod

class MinhaClasse:
    valor = 10 #Atributo de classe
    def __init__(self, nome) -> None:
        self.nome = nome  #Atributo da instância

    def metodo_instancia(self): #requer uma instância/valor para ser chamado // self recebe instancia
        return f"Método de instância chamado para {self.nome}"
    
    @classmethod
    def metodo_classe(cls): #cls recebe a classe// sempre que usar classmethod// possui acesso a todos os atributos e métodos da classe
        return f"Método da classe chamado para valor = {cls.valor}"
    
    @staticmethod
    def metodo_estatico(): #não recebe argumento, não tem acesso a atributos, faz funções específicas
        return "Método estático chamado"


    
obj = MinhaClasse(nome="Classe exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor) #Não precisa de uma instancia para acessar um atributo DA CLASSE
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())


#Exemplo do classmethod sendo usado
class Carro: #Utilizado pra criar instâncias a partir de propriedades que podemos receber, sendo elas globais ou a partir de parametro
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))
    
configuracao1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")

#Exemplo de staticmethod sendo usado

class Matematica:
    
    @staticmethod
    def somar(a,b):
        return a + b
    
print(Matematica.somar(a=10, b=15))

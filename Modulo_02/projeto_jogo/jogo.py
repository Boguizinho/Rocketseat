import random

#Definicao e criacao das classes dos jogo

#Criação da classe mae: Personagem
#Heroi: Sera controlado pelo usuario
#Inimigo: Adversario do usuario

class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}"  
    
    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4) #Dano com base no nível
        alvo.receber_ataque(dano)
        print(f"\n\033[36m{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!\033[0;0m")

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
    
    def ataque_especial(self,alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8) #Dano foi aumentado
        alvo.receber_ataque(dano)
        print(f"\033[35m{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!\033[0;0m")

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"
    
class Jogo:
    """ Classe orquestradora do jogo """

    def __init__(self) -> None:
        self.heroi = Heroi("Heroi",100,5,"Superforça")
        self.inimigo = Inimigo("Morcego",80,5,"Voador")

    def iniciar_batalha(self):
        "Fazer a gestão da batalha em turnos"
        print("\033[43mIniciando a batalha!\033[0;0m")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagens: \n")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("\nPressione Enter para atacar. . .")
            escolha = input("\nEscolha (1 - Ataque Normal, 2- Ataque Especial): ")

            if escolha == '1':
                self.heroi.atacar(self.inimigo)

            elif escolha == '2':
                self.heroi.ataque_especial(self.inimigo)

            else:
                print("Escolha inválida. Escolha novamente!")

            if self.inimigo.get_vida()> 0:
                #Inimigo ataca o heroi
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida()> 0:
            print("\n\033[32mParabéns, você venceu!\033[0;0m")
        else:
            print("\n\033[31mVocê foi derrotado!\033[0;0m")          

#Criar instancia do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()
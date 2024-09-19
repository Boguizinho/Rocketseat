def adicionar_contato(agenda,nome_contato,telefone,email):
        info = {"Nome": nome_contato, "Telefone": telefone, "Email": email, "Favorito": False}
        agenda.append(info)
        print(f"{nome_contato} foi adicionado em sua agenda de contatos!")
        return

def ver_agenda(agenda):
    print("\nLista de contatos: ")
    for indice, info in enumerate(agenda, start=1):
        status = '★' if info["Favorito"] else " "

        print(f"""{indice}. [{status}]
        Nome: {info["Nome"]} 
        Telefone: {info["Telefone"]} 
        Email: {info["Email"]}
        ---------------------------------------""")

            
def modificar_contato(agenda):
    ver_agenda(agenda)
    indice = int(input("Digite o número do contato que deseja modificar: ")) - 1

    if 0 <= indice < len(agenda):
        contato = agenda[indice]
        print(f"Dados atuais do contato {indice + 1}:")
        for chave, valor in contato.items():
            print(f"{chave}: {valor}")

        novo_nome = input("Digite o novo nome (deixe em branco para manter): ")
        novo_telefone = input("Digite o novo telefone (deixe em branco para manter): ")
        novo_email = input("Digite o novo email (deixe em branco para manter): ")

        if novo_nome:
            contato["Nome"] = novo_nome
        if novo_telefone:
            contato["Telefone"] = novo_telefone
        if novo_email:
            contato["Email"] = novo_email

        print("Contato atualizado com sucesso!")
    else:
        print("Índice de contato inválido.")

def favoritar(agenda,posicao_contato):
        posicao = int(posicao_contato) - 1
        if agenda[posicao]["Favorito"]== True:
                agenda[posicao]["Favorito"]= False
        else:
                 agenda[posicao]["Favorito"] = True
        print(f"{nome_contato} favoritado!")
       
        return

def ver_favoritos(agenda):
        print("\nLista de contatos: ")
        for indice, info in enumerate(agenda, start=1):
                status = '★' if info["Favorito"] else " "
                if status == '★': 

                        print(f"""{indice}. [{status}]
                Nome: {info["Nome"]} 
                Telefone: {info["Telefone"]} 
                Email: {info["Email"]}
        ---------------------------------------""")

def apagar_contato(agenda, posicao_contato):
      indice = int(posicao_contato) -1
      agenda.pop(indice)
      print("Contato deletado!")
      return    

agenda=[]

while True:
        print("""\n \033[33m Menu de Agenda:\033[0m
1. Adicionar contato
2. Visualizar agenda
3. Modificar contato
4. Ver contatos favoritos              
5. Favoritar/Desfavoritar contato
6. Apagar contato
7. Fechar agenda """)

        escolha = int(input("\033[33mDigite sua escolha: \033[0m\n"))

        if escolha == 1:
            nome_contato = input("Digite o nome do seu contato: \n")
            telefone = input("Digite o telefone do contato: \n")
            email = input("Digite o email do contato: \n")
            adicionar_contato(agenda, nome_contato, telefone, email)

        elif escolha == 2:
               ver_agenda(agenda)

        elif escolha == 3:
             modificar_contato(agenda)

        elif escolha == 4:
               ver_favoritos(agenda) 
                

        elif escolha == 5:
               ver_agenda(agenda)
               posicao_contato = input("Digite a posição do contato que deseja Favoritar ou Desfavoritar: ")
               favoritar(agenda, posicao_contato)

        elif escolha == 6:
                ver_agenda(agenda)
                posicao_contato = input("Digite o Nº do contato que deseja apagar: ")
                resposta = input(f"\033[31mDeseja apagar o contato Nº{posicao_contato}? (S/N): \033[0m").capitalize()
                if resposta == "S":
                        apagar_contato(agenda, posicao_contato)
                elif resposta =='N':
                        pass
                
        elif escolha == 7:
               break
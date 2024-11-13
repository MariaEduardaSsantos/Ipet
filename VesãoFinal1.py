import datetime
autorizacaoAdmin = "1603"

def menuPrincipal():
    print("\033[1;32m      ================ \033[0m")
    print("\033[1;32m       Menu Principal      \033[0m")
    print("\033[1;32m      ================ \033[0m")
    print(" ")
    print("\033[32m1.\033[0m Cadastros")
    print("\033[32m2.\033[0m Atendimentos")
    print("\033[32m3.\033[0m Consultas/Relatórios")
    print("\033[32m4.\033[0m Sair")
    print(" ")
    return input("\033[32mEscolha uma opção:\033[0m")

def menuCadastro():
    print(" ")
    print("\033[31m------------------------\033[0m")
    print("\033[31mVocê escolheu Cadastros\033[0m")
    print("\033[31m------------------------\033[0m")
    print(" ")
    print("\033[1;32m      ================  \033[0m")
    print("\033[1;32m        Menu Cadastro   \033[0m")
    print("\033[1;32m      ================  \033[0m")
    print(" ")
    print("\033[32m1.\033[0m Usuario")
    print("\033[32m2.\033[0m Clientes")
    print("\033[32m3.\033[0m Pets")
    print("\033[32m4.\033[0m Serviços(Administradores)")
    print("\033[32m5.\033[0m Voltar ao Menu Principal")
    print(" ")
    return input("\033[32mEscolha uma opção de cadastro:\033[0m")

def menuCad1():
    print(" ")
    print("\033[31m----------------------\033[0m")
    print("\033[31mVocê escolheu Usuários\033[0m")
    print("\033[31m----------------------\033[0m")
    print(" ")
    print("\033[32m1.\033[0m Cadastrar novo usuário")
    print("\033[32m2.\033[0m Atualizar")
    print("\033[32m3.\033[0m Apagar(Administradores)")
    print("\033[32m4.\033[0m Consultar")
    print("\033[32m5.\033[0m Voltar ao Menu Cadastros")
    print(" ")
    return input("\033[32mEscolha uma opção:\033[0m")

def cadastrar_usuario():
    novo_usuario = {}
    novo_usuario['Nome_Login'] = input("Digite o nome de Login: ")
    novo_usuario['Senha_Login'] = input("Digite a senha de Login: ")
    usuarios.append(novo_usuario)

def dadosCad():
    print("Dados Necessários:")
    print("1.Nome de login")
    print("2.Senha de login")
    print("3.Nome Completo")
    print("4.Email")
    print("5.Telefone")
    print("6.Endereço")

def menuAtualizarUsu():
    print(" ")
    print("\033[32mDados para Atualizar\033[0m")
    print("\033[32m1.\033[0m Nome de login")
    print("\033[32m2.\033[0m Senha de login")
    print(" ")
    return input("\033[32mDigite a opção desejada:\033[0m")

def menuCliente():
    print(" ")
    print("\033[31m-----------------------\033[0m")
    print("\033[31m Você escolheu Cliente \033[0m")
    print("\033[31m-----------------------\033[0m")
    print(" ")
    print("\033[32m1.\033[0m Cadastrar novo Cliente")
    print("\033[32m2.\033[0m Atualizar")
    print("\033[32m3.\033[0m Apagar(Administradores)")
    print("\033[32m4.\033[0m Consultar")
    print("\033[32m5.\033[0m Voltar ao Menu Cadastros")
    print(" ")
    return input("\033[32mEscolha uma opção:\033[0m")

def cadCliente():
    novo_cliente = {}
    novo_cliente['Nome_Cliente'] = input("Digite o nome do Cliente: ")
    novo_cliente['Nome_Pet'] = input("Digite o nome do Pet: ")
    novo_cliente['Raça_Pet'] = input("Digite a raça do Pet: ")
    novo_cliente['Email_Cliente'] = input("Digite o email do Cliente: ")
    novo_cliente['Telefone_Cliente'] = input("Digite o telefone do Cliente: ")
    novo_cliente['Endereço_Cliente'] = input("Digite o endereço Cliente: ")
    clientes.append(novo_cliente)

def dadoAtualizaCliente():
    print(" ")
    print("\033[32mDados para Atualizar\033[0m")
    print("\033[32m1.\033[0m Nome Completo")
    print("\033[32m2.\033[0m Nome do pet")
    print("\033[32m3.\033[0m Raça do pet")
    print("\033[32m4.\033[0m Email")
    print("\033[32m5.\033[0m Telefone")
    print("\033[32m6.\033[0m Endereço")
    print(" ")
    return input("\033[32mEscolha uma opção:\033[0m")

def dadoCliente():
    print("1.Nome Completo")
    print("2.Nome do pet")
    print("3.Raça do pet")
    print("4.Email")
    print("5.Telefone")
    print("6.Endereço")

def menuPet():
    print(" ")
    print("\033[31m---------------------\033[0m")
    print("\033[31m  Você escolheu Pets \033[0m")
    print("\033[31m---------------------\033[0m")
    print(" ")
    print("\033[32m1.\033[0m Cadastrar novo Pet")
    print("\033[32m2.\033[0m Atualizar")
    print("\033[32m3.\033[0m Apagar(Administrador)")
    print("\033[32m4.\033[0m Consultar")
    print("\033[32m5.\033[0m Voltar ao Menu Cadastros")
    print(" ")
    return input("\033[32mEscolha uma opção:\033[0m")

def cadastro_Pet():
    novoPet = {}
    print("Dados do Pet")
    novoPet['Nome_Pet'] = input("Digite o Nome do Pet:")
    novoPet['Sexo_Pet'] = input("Digite o Sexo do Pet:")
    novoPet['Raça_Pet'] = input("Digite a Raça do Pet:")
    novoPet['Nome_Dono'] = input("Digite o Nome do Dono(a):")
    novoPet['Telefone_Dono'] = input("Digite o Telefone do Dono(a):")
    novoPet['Endereço_Dono'] = input("Digite o Endereço do Dono(a):")
    pets.append(novoPet)

def atualizaPet():
    print(" ")
    print("\033[32mDados para Atualizar\033[0m")
    print("\033[32m1.\033[0m Nome do Pet.")
    print("\033[32m2.\033[0m Sexo do Pet.")
    print("\033[32m3.\033[0m Raça do Pet.")
    print("\033[32m4.\033[0m Nome do Dono(a).")
    print("\033[32m5.\033[0m Telefone do Dono(a).")
    print("\033[32m6.\033[0m Endereço do Dono(a)")
    print(" ")
    return input("\033[32mEscolha uma opção:\033[0m")

def menuAdmin():
    print(" ")
    print("\033[32m1.\033[0m Apagar Usuário")
    print("\033[32m2.\033[0m Apagar Cliente")
    print("\033[32m3.\033[0m Apagar Pet")
    print("\033[32m4.\033[0m Voltar ao menu Cadastro")
    print(" ")
    return input("\033[32mEscolha uma opção:\033[0m")

def menuAtendimentos():
    print(" ")
    print("\033[1;31m      ====================  \033[0m")
    print("\033[1;31m        Menu Atendimentos   \033[0m")
    print("\033[1;31m      ====================  \033[0m")
    print("\033[31m1.\033[0m Iniciar")
    print("\033[31m2.\033[0m Agendar(Pets Cadastrados)")
    print("\033[31m3.\033[0m Remarcar")
    print("\033[31m4.\033[0m Voltar ao Menu Principal")
    print(" ")
    return input("\033[31mEscolha uma opção:\033[0m")

def iniciarAtendimentos():
    iniciarAten = {}
    print(" ")
    print("\033[32m-----------------------------------\033[0m")
    print("\033[32m Você escolheu Iniciar Atendimento \033[0m")
    print("\033[32m-----------------------------------\033[0m")
    print(" ")
    iniciarAten['Nome_Pet'] = input("Digite o nome do pet:")
    iniciarAten['Raca_Pet'] = input("Digite a raça do pet:")
    iniciarAten['Sx_Pet'] = input("Digite o sexo do Pet:")
    iniciarAten['Nome_do_Dn'] = input("Digite o nome do dono:")
    iniciarAten['Telefone_Dn'] = input("Digite o telefone do dono:")
    iniciarAten['Endereco_Dn'] = ("Digite o endereço do dono:")
    iniciarAten['Tipo_Aten'] = input("Digite o tipo de atendimento:")
    
    atendimentos.append(iniciarAten)

def agendarAtendimentos():
    print(" ")
    print("\033[32m-----------------------------------\033[0m")
    print("\033[32m Você escolheu Agendar Atendimento \033[0m")
    print("\033[32m-----------------------------------\033[0m")
    print(" ")
    print("\033[31mOPCÕES\033[0m")
    print("\033[31m1.\033[0m Banho")
    print("\033[31m2.\033[0m Banho e Tosa")
    print("\033[31m3.\033[0m Tosa")
    print("\033[31m4.\033[0m Consulta Médica")
    print("\033[31m5.\033[0m Adestramento")
    print("\033[31m6.\033[0m Castração")
    print("\033[31m7.\033[0m Voltar ao menu atendimentos")
    print(" ")
    return input("\033[31mEscolha uma opção:\033[0m")

def menuRemarcar():
    print(" ")
    print("\033[32m-----------------------------------\033[0m")
    print("\033[32m Você escolheu Remarcar Atendimento \033[0m")
    print("\033[32m-----------------------------------\033[0m")
    print(" ")
    print("\033[31m1.\033[0m Remarcar Horário:")
    print("\033[31m2.\033[0m Remarcar Data:")
    print(" ")
    return input("\033[31mEscolha uma opção:\033[0m")

def menuRem():
    print(" ")
    print("\033[31mOPCÕES\033[0m")
    print("\033[31m1.\033[0m Banho")
    print("\033[31m2.\033[0m Banho e Tosa")
    print("\033[31m3.\033[0m Tosa")
    print("\033[31m4.\033[0m Consulta Médica")
    print("\033[31m5.\033[0m Adestramento")
    print("\033[31m6.\033[0m Castração")
    print("\033[31m7.\033[0m Voltar ao menu atendimentos")
    print(" ")
    return input("\033[31mEscolha uma opção:\033[0m")

def menuConRela():
    print(" ")
    print("\033[1;32m      =========================================  \033[0m")
    print("\033[1;32m        Menu Atendimentos Consultas/Relatórios   \033[0m")
    print("\033[1;32m      =========================================  \033[0m")
    print(" ")
    print("\033[32m1.\033[0m Consultas")
    print("\033[32m2.\033[0m Relatórios")
    print("\033[32m3.\033[0m Voltar ao Menu Principal")
    print(" ")
    return input("\033[31mEscolha uma opção:\033[0m")

def menuConsu():
    print(" ")
    print("\033[31m-------------------------\033[0m")
    print("\033[31m Você escolheu Consultas \033[0m")
    print("\033[31m-------------------------\033[0m")
    print(" ")
    print("\033[32m1.\033[0m Consular Usuários")
    print("\033[32m2.\033[0m Consultar Clientes")
    print("\033[32m3.\033[0m Consultar Pets")
    print("\033[32m4.\033[0m Voltar ao Menu Consulta/Relatório")
    print(" ")
    return input("\033[32mEscolha uma opção:\033[0m")

def menuRela():
    print(" ")
    print("\033[31m--------------------------\033[0m")
    print("\033[31m Você escolheu Relatórios \033[0m")
    print("\033[31m--------------------------\033[0m")
    print(" ")
    print("\033[32m1.\033[0m Banho")
    print("\033[32m2.\033[0m Banho e Tosa")
    print("\033[32m3.\033[0m Tosa")
    print("\033[32m4.\033[0m Consulta Médica")
    print("\033[32m5.\033[0m Castração")
    print("\033[32m6.\033[0m Adestramento")
    print("\033[32m7.\033[0m Todos os Atendimetos")
    print("\033[32m8.\033[0m Voltar ao Menu Consulta/Relatório")
    print(" ")
    return input("\033[32mEscolha uma opção:\033[0m")

def validar_data(dataAtendimento):
    try:
        datetime.datetime.strptime(dataAtendimento, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def validar_horario(horarioAtendimento):
    try:
        datetime.datetime.strptime(horarioAtendimento, "%H:%M")
        return True
    except ValueError:
        return False

atendimentos = []
banhos = []
banhoDd = {}
banhoEtosa = []
banhoetDd = {}
tosa = []
tosaDd = {}
consultaMed = []
consuDd = {}
adestramento = []
adesDd = {}
castracao = []
castDd = {}

usuarioslo = []
usuarios = []
clientes = []
pets = []
continuar = True

import pyfiglet
result = pyfiglet.figlet_format("   IPET      ")
print("\033[1;31m" + result + "\033[0m")

while True:
    opcao = input("\033[32m1 - Cadastrar\n2 - Login\nEscolha uma opção:\033[0m")

    if opcao == '1':
        nome_usuario = input("Nome de usuário: ")
        senha = input("Senha: ")
        if any(usuario['Nome_Login'] == nome_usuario for usuario in usuarios):
            print("\033[31mUsuário já existe!\033[0m")
        else:
            usuarios.append({'Nome_Login': nome_usuario, 'Senha_Login': senha})
            print("\033[31mUsuário cadastrado com sucesso!\033[0m")

    elif opcao == '2':
        nome_usuario = input("Nome de usuário: ")
        senha = input("Senha: ")

        for usuario in usuarios:
            if usuario['Nome_Login'] == nome_usuario and usuario['Senha_Login'] == senha:
                print("\033[31mUsuário autenticado!\033[0m")
                print("\033[32mAbrindo Programa!\033[0m")
        break
    else:
        print("\033[31mOpção inválida!\033[0m")

while True:
    print(" ")
    opcao = menuPrincipal()
    if opcao == "1":
        while True:
            opcaoCadastro = menuCadastro()
            if opcaoCadastro == "1":
                    while True:
                        opcaoCad1 = menuCad1()
                        if opcaoCad1 == "1":
                            print(" ")
                            print("\033[31mVocê escolheu Cadastrar novo Usuário\033[0m")
                            print("\033[31m------------------------------------\033[0m")
                            cadastrar_usuario()

                        elif opcaoCad1 == "2":
                            print(" ")
                            print("\033[31mVocê escolheu Atualizar Dado do Usuário\033[0m")
                            print("\033[31m------------------------------------\033[0m")
                            nome_usuario = input("\033[32mDigite o nome do usuário: \033[0m")
                            usuario_encontrado = None
                            for usuario in usuarios:
                                if usuario['Nome_Login'] == nome_usuario:
                                    usuario_encontrado = usuario
                                    break
                            if usuario_encontrado:
                                atualizaDd = menuAtualizarUsu()
                                print(" ")
                            if atualizaDd == '1':
                                novo_nome = input("Digite o novo nome de login: ")
                                usuario['Nome_Login'] = novo_nome
                                print("\033[31mDado Atualizado\033[0m")
                            elif atualizaDd == "2":
                                nova_senha = input("Digite a nova senha de login: ")
                                usuario['Senha_Login'] = nova_senha
                                print("\033[31mDado Atualizado\033[0m")
                            else:
                                print("\033[32mUsuário não Existe\033[0m")

                        elif opcaoCad1 == "4":
                            print(" ")
                            print("\033[31mVocê escolheu Consultar Usuário\033[0m")
                            print("\033[31m------------------------------------\033[0m")
                            nome_login = input("\033[32mDigite o nome de Login para Consultar: \033[0m")
                            for usuario in usuarios:
                                if usuario['Nome_Login'] == nome_login:
                                    print("Usuário encontrado:")
                                    for chave, valor in usuario.items():
                                        print(f"{chave}: {valor}")
                                    break
                            else:
                                print("Usuário não encontrado.")

                        elif opcaoCad1 == "4":
                            print(" ")
                            print("\033[31mVocê escolheu Consultar Usuário\033[0m")
                            print("\033[31m------------------------------------\033[0m")
                            nome_login = input("\033[32mDigite o nome de Login para Consultar: \033[0m")
                            for i in usuarios:
                                if usuario[i][0] == nome_login:
                                    print(usuario)
                                    break
                            else:
                                print("\033[32mUsuário não encontrado.\033[0m")


                        elif opcaoCad1 == "5":
                            break
            
            if opcaoCadastro == "2":        
                    while True:
                        opcaoCad2 = menuCliente()
                        if opcaoCad2 == "1":
                            print(" ")
                            print("\033[31mVocê escolheu Cadastrar novo Cliente\033[0m")
                            print("\033[31m------------------------------------\033[0m")
                            cadCliente()

                        elif opcaoCad2 == "2":
                            print(" ")
                            print("\033[31mVocê escolheu Atualizar Dado do Cliente\033[0m")
                            print("\033[31m------------------------------------\033[0m")
                            nome_cliente = input("\033[32mDigite o nome do Cliente:\033[0m")
                            cliente_encontrado = None
                            for cliente in clientes:
                                if cliente['Nome_Cliente'] == nome_cliente:
                                    cliente_encontrado = cliente
                                    break
                            if cliente_encontrado:
                                atualizaDdCli = dadoAtualizaCliente()
                            if atualizaDdCli == '1':
                                novo_nome = input("Digite o novo nome do cliente: ")
                                cliente['Nome_Cliente'] = novo_nome
                                print("\033[31mDado Atualizado\033[0m")
                            elif atualizaDdCli == "2":
                                novo_nomePet = input("Digite o novo nome do Pet: ")
                                cliente['Nome_Pet'] = novo_nomePet
                                print("\033[31mDado Atualizado\033[0m")
                            elif atualizaDdCli == "3":
                                nova_racaPet = input("Digite a nova Raça do Pet: ")
                                cliente['Raça_Pet'] = nova_racaPet
                                print("\033[31mDado Atualizado\033[0m")
                            elif atualizaDdCli == "4":
                                novo_email = input("Digite o novo Email: ")
                                cliente['Email_Cliente'] = novo_email
                                print("\033[31mDado Atualizado\033[0m")
                            elif atualizaDdCli == "5":
                                novo_telefone = input("Digite o novo Telefone: ")
                                cliente['Telefone_Cliente'] = novo_telefone
                                print("\033[31mDado Atualizado\033[0m")
                            elif atualizaDdCli == "6":
                                novo_endereco = input("Digite o novo endereço: ")
                                cliente['Endereço_Cliente'] = novo_endereco
                                print("\033[31mDado Atualizado\033[0m")
                            else:
                                print("\033[32mCliente não existe\033[0m")

                        elif opcaoCad2 == "3":
                            print(" ")
                            print("\033[31mVocê escolheu Apagar Cliente\033[0m")
                            print("\033[31m----------------------------\033[0m")
                            autorizacaoAdmin = input("\033[32mDigite a senha de admin para apagar:\033[0m")
                            if autorizacaoAdmin == "1603":
                                nomedoCliApaga = input("Nome do Cliente que quer apagar:")
                                for i in range(len(clientes) - 1, -1, -1):
                                    if clientes[i]['Nome_Cliente'] == nomedoCliApaga:
                                        del clientes[i]
                                        print("\033[31mCliente Apagado\033[0m")
                                        break
                                    else:
                                        print("\033[32mCliente não Existe\033[0m")                
                            else:
                                print("\033[32mVocê não tem autorização\033[0m")

                        elif opcaoCad2 == "4":
                            print(" ")
                            print("\033[31mVocê escolheu Consultar Cliente\033[0m")
                            print("\033[31m-------------------------------\033[0m")
                            nome_Cliente = input("\033[32mDigite o nome do Cliente para consultar:\033[0m")
                            for cliente in clientes:
                                if cliente['Nome_Cliente'] == nome_Cliente:
                                    print(" ")
                                    for chave, valor in cliente.items():
                                        print(f"{chave}: {valor}")
                                    break
                            else:
                                print("\033[32mCliente não encontrado.\033[0m")


                        elif opcaoCad2 == "5":
                            break
                            
            if opcaoCadastro == "3":        
                    while True:
                        opcaoCad3 = menuPet()
                        if opcaoCad3 == "1":
                            print(" ")
                            print("\033[31mVocê escolheu Cadastrar novo Pet\033[0m")
                            print("\033[31m------------------------------------\033[0m")
                            cadastro_Pet()

                        elif opcaoCad3 == "2":
                            print(" ")
                            print("\033[31mVocê escolheu Atualizar Dado do Pet\033[0m")
                            print("\033[31m------------------------------------\033[0m")
                            nome_pet = input("\033[32mDigite o nome do Pet:\033[0m")
                            pet_encontrado = None
                            for pet in pets:
                                if pet['Nome_Pet'] == nome_pet:
                                    pet_encontrado = pet
                                    break
                            if pet_encontrado:
                                atualizaDdPet = atualizaPet()
                            if atualizaDdPet == '1':
                                novo_nome = input("Digite o Novo nome do Pet: ")
                                pet['Nome_Pet'] = novo_nome
                                print("\033[31mDado Atualizado\033[0m")
                            elif atualizaDdPet == "2":
                                sexo_Pet = input("Digite Sexo do Pet: ")
                                pet['Sexo_Pet'] = sexo_Pet
                                print("\033[31mDado Atualizado\033[0m")
                            elif atualizaDdPet == "3":
                                nova_racaPet = input("Digite a nova Raça do Pet: ")
                                pet['Raça_Pet'] = nova_racaPet
                                print("\033[31mDado Atualizado\033[0m")
                            elif atualizaDdPet == "4":
                                novo_NomeDono = input("Digite o novo Nome do Dono(a): ")
                                pet['Nome_Dono'] = novo_NomeDono
                                print("\033[31mDado Atualizado\033[0m")
                            elif atualizaDdPet == "5":
                                novo_telefone = input("Digite o novo Telefone do Dono(a): ")
                                pet['Telefone_Dono'] = novo_telefone
                                print("\033[31mDado Atualizado\033[0m")
                            elif atualizaDdPet == "6":
                                novo_endereco = input("Digite o novo Endereço do Dono(a): ")
                                pet['Endereço_Dono'] = novo_endereco
                                print("\033[31mDado Atualizado\033[0m")
                            else:
                                print("\033[32mPet não existe\033[0m")

                        elif opcaoCad3 == "3":
                            print(" ")
                            print("\033[31mVocê escolheu Apagar Pet\033[0m")
                            print("\033[31m----------------------------\033[0m")
                            autorizacaoAdmin = input("\033[32mDigite a senha de admin para apagar:\033[0m")
                            if autorizacaoAdmin == "1603":
                                nomedoPetApaga = input("Nome do Pet que quer apagar:")
                                for i in range(len(pets) - 1, -1, -1):
                                    if pets[i]['Nome_Pet'] == nomedoPetApaga:
                                        del pets[i]
                                        print("\033[31mPet Apagado\033[0m")
                                        break
                                    else:
                                        print("\033[32mPet não existe\033[0m")                
                            else:
                                print("\033[32mVocê não tem autorização\033[0m")

                        elif opcaoCad3 == "4":
                            print(" ")
                            print("\033[31mVocê escolheu Consultar Pet\033[0m")
                            print("\033[31m-------------------------------\033[0m")
                            nome_pet = input("\033[32mDigite o nome do Pet para consultar:\033[0m")
                            for pet in pets:
                                if pet['Nome_Pet'] == nome_pet:
                                    print(" ")
                                    for chave, valor in pet.items():
                                        print(f"{chave}: {valor}")
                                    break
                            else:
                                print("\033[32Pet não encontrado.\033[0m")


                        elif opcaoCad3 == "5":
                            break

            elif opcaoCadastro == "4":
                while True:
                    print(" ")
                    print("\033[31m--------------------------------------\033[0m")
                    print("\033[31mVocê escolheu Serviços Administradores\033[0m")
                    print("\033[31m--------------------------------------\033[0m")
                    print(" ")
                    senhaAdmin = input("Digite a senha de Admin para entrar:")
                    if senhaAdmin == "1603":
                        print("\033[32mSenha correta\033[0m")
                        opcaoCad4 = menuAdmin()
                        if opcaoCad4 == "1":
                            nomedoUsuApaga = input("\033[32Nome usuário que quer apagar:\033[0m")
                            for i in range(len(usuarios) - 1, -1, -1):
                                if usuarios[i]['Nome_Login'] == nomedoUsuApaga:
                                    del usuarios[i]
                                    print("\033[31mUsuário Apagado\033[0m")                                        
                                    break
                                else:
                                    print("\033[32Usuário não Existe\033[0m")
                        if opcaoCad4 == "2":
                            nomedoCliApaga = input("\033[32Nome do Cliente que quer apagar:\033[0m")
                            for i in range(len(clientes) - 1, -1, -1):
                                if clientes[i]['Nome_Cliente'] == nomedoCliApaga:
                                    del clientes[i]
                                    print("\033[31mCliente Apagado\033[0m")
                                    break
                                else:
                                    print("\033[32Cliente não Existe\033[0m")
                        if opcaoCad4 == "3":
                            nomedoPetApaga = input("\033[32mNome do pet que quer Apagar:\033[0m")
                            for i in range(len(pets) - 1, -1, -1):
                                if pets[i]['Nome_Pet'] == nomedoPetApaga:
                                    del pets[i]
                                    print("\033[31mPet Apagado\033[0m")
                                    break
                                else:
                                    print("\033[32Pet não Existe\033[0m")
                        if opcaoCad4 == "4":
                            break

            elif opcaoCadastro == "5":
                break
    
    elif opcao == "2":
        while True:

            opcaoaten = menuAtendimentos()
            if opcaoaten == "1":
                while True:
                    iniciarAtendimentos()
                    break

            elif opcaoaten == "2":
                while True:
                    opcaoAge = agendarAtendimentos()
                    if opcaoAge == "1":
                        print(" ")
                        print("\033[31mVocê escolheu Banho\033[0m")
                        print("\033[31m-------------------\033[0m")
                        nomePet = input("\033[31mDigite o nome do pet:\033[0m")
                        for pet in pets:
                            if pet['Nome_Pet'] == nomePet:
                                print(" ")
                                print("\033[32mPet já cadastrado\033[0m")
                                banhoDd['NomedoPet'] = pet['Nome_Pet']
                                print(" ")
                                while True:
                                    dataAtendimento = input("Digite a data do banho no formato DD/MM/AAAA: ")
                                    if validar_data(dataAtendimento):
                                        break
                                    else:
                                        print("Data inválida. Por favor, digite a data no formato DD/MM/AAAA.")
                                banhoDd['Data_Atendimento'] = dataAtendimento
                                while True:
                                    horarioAtendimento = input("Digite o horário do Banho no formato HH:MM: ")
                                    if validar_horario(horarioAtendimento):
                                        break
                                    else:
                                        print("Horário inválido. Por favor, digite o horário no formato HH:MM.")
                                banhoDd['Horário_Atendimento'] = horarioAtendimento
                                obs = input("Alguma observação:")
                                banhoDd['Obs'] = obs
                                banhos.append(banhoDd)
                                atendimentos.append(banhos)
                            else:
                                print(" ")
                                print("\033[32mPet não Cadastrado\033[0m")

                    elif opcaoAge == "2":   
                        print(" ")
                        print("\033[31mVocê escolheu Banho e Tosa\033[0m")
                        print("\033[31m--------------------------\033[0m")
                        nomePet = input("\033[31mDigite o nome do pet:\033[0m")
                        for pet in pets:
                            if pet['Nome_Pet'] == nomePet:
                                print(" ")
                                print("\033[32mPet já cadastrado\033[0m")
                                banhoetDd['NomedoPet'] = pet['Nome_Pet']
                                while True:
                                    dataAtendimento = input("Digite a data do Banho Tosa no formato DD/MM/AAAA: ")
                                    if validar_data(dataAtendimento):
                                        break
                                    else:
                                        print("Data inválida. Por favor, digite a data no formato DD/MM/AAAA.")
                                banhoDd['Data_Atendimento'] = dataAtendimento
                                while True:
                                    horarioAtendimento = input("Digite o horário do Banho Tosa no formato HH:MM: ")
                                    if validar_horario(horarioAtendimento):
                                        break
                                    else:
                                        print("Horário inválido. Por favor, digite o horário no formato HH:MM.")
                                banhoetDd['Horário_Atendimento'] = horarioAtendimento
                                obs = input("Alguma observação:")
                                banhoetDd['Obs'] = obs
                                banhoEtosa.append(banhoetDd)
                                atendimentos.append(banhoEtosa)
                            else:
                                print(" ")
                                print("\033[32mPet não Cadastrado\033[0m")    

                    elif opcaoAge == "3":   
                        print(" ")
                        print("\033[31mVocê escolheu Tosa\033[0m")
                        print("\033[31m------------------\033[0m")
                        nomePet = input("\033[31mDigite o nome do pet:\033[0m")
                        for pet in pets:
                            if pet['Nome_Pet'] == nomePet:
                                print(" ")
                                print("\033[32mPet já cadastrado\033[0m")
                                tosaDd['NomedoPet'] = pet['Nome_Pet']
                                while True:
                                    dataAtendimento = input("Digite a data da Tosa no formato DD/MM/AAAA: ")
                                    if validar_data(dataAtendimento):
                                        break
                                    else:
                                        print("Data inválida.")
                                tosaDd['Data_Atendimento'] = dataAtendimento
                                while True:
                                    horarioAtendimento = input("Digite o horário da Tosa no formato HH:MM: ")
                                    if validar_horario(horarioAtendimento):
                                        break
                                    else:
                                        print("Horário inválido. Por favor, digite o horário no formato HH:MM:SS.")
                                tosaDd['Horário_Atendimento'] = horarioAtendimento
                                obs = input("Alguma observação:")
                                tosaDd['Obs'] = obs
                                tosa.append(tosaDd)
                                atendimentos.append(tosa)
                            else:
                                print(" ")
                                print("\033[32mPet não Cadastrado\033[0m")    
               
                    elif opcaoAge == "4":   
                        print(" ")
                        print("\033[31mVocê escolheu Consulta Médica\033[0m")
                        print("\033[31m-----------------------------\033[0m")
                        nomePet = input("\033[31mDigite o nome do pet:\033[0m")
                        for pet in pets:
                            if pet['Nome_Pet'] == nomePet:
                                print(" ")
                                print("\033[32mPet já cadastrado\033[0m")
                                consuDd['NomedoPet'] = pet['Nome_Pet']
                                while True:
                                    dataAtendimento = input("Digite a data da Consulta no formato DD/MM/AAAA: ")
                                    if validar_data(dataAtendimento):
                                        break
                                    else:
                                        print("Data inválida.")
                                consuDd['Data_Atendimento'] = dataAtendimento
                                while True:
                                    horarioAtendimento = input("Digite o horário da Consulta no formato HH:MM: ")
                                    if validar_horario(horarioAtendimento):
                                        break
                                    else:
                                        print("Horário inválido. Por favor, digite o horário no formato HH:MM:SS.")
                                consuDd['Horário_Atendimento'] = horarioAtendimento
                                sintomasMed = input("Quais sintomas:")
                                consuDd['Sintomas'] = sintomasMed
                                exames = input("Fez algum exame:")
                                consuDd['Exames'] = exames
                                obs = input("Alguma observação:")
                                consuDd['Obs'] = obs
                                consultaMed.append(consuDd)
                                atendimentos.append(consultaMed)
                            else:
                                print(" ")
                                print("\033[32mPet não Cadastrado\033[0m")            

                    elif opcaoAge == "5":   
                        print(" ")
                        print("\033[31mVocê escolheu Adestramento\033[0m")
                        print("\033[31m--------------------------\033[0m")
                        nomePet = input("\033[31mDigite o nome do pet:\033[0m")
                        for pet in pets:
                            if pet['Nome_Pet'] == nomePet:
                                print(" ")
                                print("\033[32mPet já cadastrado\033[0m")
                                adesDd['NomedoPet'] = pet['Nome_Pet']
                                while True:
                                    dataAtendimento = input("Digite a data de início do adestramento no formato DD/MM/AAAA: ")
                                    if validar_data(dataAtendimento):
                                        break
                                    else:
                                        print("Data inválida.")
                                    adesDd['Data_Atendimento'] = dataAtendimento
                                while True:
                                    horarioAtendimento = input("Digite o horário das sessões no formato HH:MM: ")
                                    if validar_horario(horarioAtendimento):
                                        break
                                    else:
                                        print("Horário inválido. Por favor, digite o horário no formato HH:MM:SS.")
                                adesDd['Horário_Atendimento'] = horarioAtendimento
                                quantsessoes = input("Digite a quantidade de sessões:")
                                adesDd['Quantidade_Sessões'] = quantsessoes
                                obs = input("Alguma observação:")
                                adesDd['Obs'] = obs
                                adestramento.append(adesDd)
                                atendimentos.append(adestramento)
                            else:
                                print(" ")
                                print("\033[32mPet não Cadastrado\033[0m")    
                
                    elif opcaoAge == "6":
                        print(" ")
                        print("\033[31mVocê escolheu Castração\033[0m")
                        print("\033[31m-----------------------\033[0m")
                        nomePet = input("\033[31mDigite o nome do pet:\033[0m")
                        for pet in pets:
                            if pet['Nome_Pet'] == nomePet:
                                print(" ")
                                print("\033[32mPet já cadastrado\033[0m")
                                castDd['NomedoPet'] = pet['Nome_Pet']
                                while True:
                                    dataAtendimento = input("Digite a data da Castração no formato DD/MM/AAAA: ")
                                    if validar_data(dataAtendimento):
                                        break
                                    else:
                                        print("Data inválida. Por favor, digite a data no formato DD/MM/AAAA.")
                                castDd['Data_Atendimento'] = dataAtendimento
                                while True:
                                    horarioAtendimento = input("Digite o horário da Castração no formato HH:MM: ")
                                    if validar_horario(horarioAtendimento):
                                        break
                                    else:
                                        print("Horário inválido. Por favor, digite o horário no formato HH:MM.")
                                castDd['Horário_Atendimento'] = horarioAtendimento
                                obs = input("Alguma observação:")
                                castDd['Obs'] = obs
                                castracao.append(castDd)
                                atendimentos.append(castracao)
                            else:
                                print(" ")
                                print("\033[32mPet não Cadastrado\033[0m")            
                
                    elif opcaoAge == "7":
                        break

            elif opcaoaten == "3":
                opcaoRem = menuRemarcar()
                if opcaoRem == "1":
                    while True:
                        print(" ")
                        print("\033[31mVocê escolheu Remarcar Horário\033[0m")
                        print("\033[31m------------------------------\033[0m")
                        opRem = menuRem()
                        if opRem == "1":
                            for i in banhos:
                                print(" ")
                                print("\033[31mBANHO\033[0m")
                                nomePet = input("Digite o nome do pet:")
                                for pet in pets:
                                    if pet['Nome_Pet'] == nomePet:
                                        while True:
                                            horarioAtendimento = input("Digite o novo horário do Banho no formato HH:MM: ")
                                            if validar_horario(horarioAtendimento):
                                                break
                                            else:
                                                print("Horário inválido. Por favor, digite o horário no formato HH:MM.")
                                        banhoDd['Data_Atendimento'] = horarioAtendimento
                                        print("\033[31mHorário Remarcado\033[0m")
                                    else:
                                        print("\033[32mSem horário Agendado\033[0m")

                        elif opRem == "2":
                            for i in banhoEtosa:
                                print(" ")
                                print("\033[31mBANHO E TOSA\033[0m")
                                nomePet = input("Digite o nome do pet:")
                                for pet in pets:
                                    if pet['Nome_Pet'] == nomePet:
                                        while True:
                                            horarioAtendimento = input("Digite o novo horário do Banho e Tosa no formato HH:MM: ")
                                            if validar_horario(horarioAtendimento):
                                                break
                                            else:
                                                print("Horário inválido. Por favor, digite o horário no formato HH:MM.")
                                        banhoetDd['Horário_Atendimento'] = horarioAtendimento
                                        print("\033[31mHorário Remarcado\033[0m")
                                    else:
                                        print("\033[32mSem horário Agendado\033[0m")

                        elif opRem == "3":
                            for i in tosa:
                                print(" ")
                                print("\033[31mTOSA\033[0m")
                                nomePet = input("Digite o nome do pet:")
                                for pet in pets:
                                    if pet['Nome_Pet'] == nomePet:
                                        while True:
                                            horarioAtendimento = input("Digite o novo horário da Tosa no formato HH:MM: ")
                                            if validar_horario(horarioAtendimento):
                                                break
                                            else:
                                                print("Horário inválido. Por favor, digite o horário no formato HH:MM.")
                                        tosaDd['Horário_Atendimento'] = horarioAtendimento
                                        print("\033[31mHorário Remarcado\033[0m")
                                    else:
                                        print("\033[32mSem horário Agendado\033[0m")

                        elif opRem == "4":
                            for i in consultaMed:
                                print(" ")
                                print("\033[31mCONSULTA MÉDICA\033[0m")
                                nomePet = input("Digite o nome do pet:")
                                for pet in pets:
                                    if pet['Nome_Pet'] == nomePet:
                                        while True:
                                            horarioAtendimento = input("Digite o novo horário da Consulta no formato HH:MM: ")
                                            if validar_horario(horarioAtendimento):
                                                break
                                            else:
                                                print("Horário inválido. Por favor, digite o horário no formato HH:MM.")
                                        consuDd['Horário_Atendimento'] = horarioAtendimento
                                        print("\033[31mHorário Remarcado\033[0m")
                                    else:
                                        print("\033[32mSem horário Agendado\033[0m")

                        elif opRem == "5":
                            for i in adestramento:
                                print(" ")
                                print("\033[31mADESTRAMENTO\033[0m")
                                nomePet = input("Digite o nome do pet:")
                                for pet in pets:
                                    if pet['Nome_Pet'] == nomePet:
                                        while True:
                                            horarioAtendimento = input("Digite o novo horário do Adestramento no formato HH:MM: ")
                                            if validar_horario(horarioAtendimento):
                                                break
                                            else:
                                                print("Horário inválido. Por favor, digite o horário no formato HH:MM.")
                                            adesDd['Horário_Atendimento'] = horarioAtendimento
                                            print("\033[31mHorário Remarcado\033[0m")
                                    else:
                                        print("\033[32mSem horário Agendado\033[0m")

                        elif opRem == "6":
                            for i in castracao:
                                print(" ")
                                print("\033[31mCASTRAÇÃO\033[0m")
                                nomePet = input("Digite o nome do pet:")
                                for pet in pets:
                                    if pet['Nome_Pet'] == nomePet:
                                        while True:
                                            horarioAtendimento = input("Digite o novo horário da Castração no formato HH:MM: ")
                                            if validar_horario(horarioAtendimento):
                                                break
                                            else:
                                                print("Horário inválido. Por favor, digite o horário no formato HH:MM.")
                                        castDd['Horário_Atendimento'] = horarioAtendimento
                                        print("\033[31mHorário Remarcado\033[0m")
                                    else:
                                        print("\033[32mSem horário Agendado\033[0m")

                        elif opRem == "7":
                            break
            
                elif opcaoRem == "2":
                    while True:
                        print(" ")
                        print("\033[31mVocê escolheu Remarcar Data\033[0m")
                        print("\033[31m------------------------------\033[0m")
                        opRem1 = menuRem()
                        if opRem1 == "1":
                            for i in banhos:
                                print(" ")
                                print("\033[31mBANHO\033[0m")
                                nomePet = input("Digite o nome do pet:")
                                for pet in pets:
                                    if pet['Nome_Pet'] == nomePet:
                                        while True:
                                            dataAtendimento = input("Digite a nova Data do Banho no formato DD/MM/AAAA: ")
                                            if validar_data(dataAtendimento):
                                                break
                                            else:
                                                print("Data inválida. Por favor, digite a data no formato DD/MM/AAAA.")
                                        banhoDd['Data_Atendimento'] = dataAtendimento
                                        print("\033[31mData Remarcada\033[0m")
                                    else:
                                        print("\033[32mSem data Agendada\033[0m")

                        elif opRem1 == "2":
                            for i in banhoEtosa:
                                print(" ")
                                print("\033[31mBANHO E TOSA\033[0m")
                                nomePet = input("Digite o nome do pet:")
                                for pet in pets:
                                    if pet['Nome_Pet'] == nomePet:
                                        while True:
                                            dataAtendimento = input("Digite a nova Data do Banho e Tosa no formato DD/MM/AAAA: ")
                                            if validar_data(dataAtendimento):
                                                break
                                            else:
                                                print("Data inválida. Por favor, digite a data no formato DD/MM/AAAA.")
                                        banhoetDd['Data_Atendimento'] = dataAtendimento
                                        print("\033[31mData Remarcada\033[0m")
                                    else:
                                        print("\033[32mSem data Agendada\033[0m")

                        elif opRem1 == "3":
                            for i in tosa:
                                print(" ")
                                print("\033[31mTOSA\033[0m")
                                nomePet = input("Digite o nome do pet:")
                                for pet in pets:
                                    if pet['Nome_Pet'] == nomePet:
                                        while True:
                                            dataAtendimento = input("Digite a nova Data da Tosa no formato DD/MM/AAAA: ")
                                            if validar_data(dataAtendimento):
                                                break
                                            else:
                                                print("Data inválida. Por favor, digite a data no formato DD/MM/AAAA.")
                                        tosaDd['Data_Atendimento'] = dataAtendimento
                                        print("\033[31mData Remarcada\033[0m")
                                    else:
                                        print("\033[32mSem data Agendada\033[0m")

                        elif opRem1 == "4":
                            for i in consultaMed:
                                print(" ")
                                print("\033[31mCONSULTA MÉDICA\033[0m")
                                nomePet = input("Digite o nome do pet:")
                                for pet in pets:
                                    if pet['Nome_Pet'] == nomePet:
                                        while True:
                                            dataAtendimento = input("Digite a nova Data da Consulta no formato DD/MM/AAAA: ")
                                            if validar_data(dataAtendimento):
                                                break
                                            else:
                                                print("Data inválida. Por favor, digite a data no formato DD/MM/AAAA.")
                                        consuDd['Data_Atendimento'] = dataAtendimento
                                        print("\033[31mData Remarcada\033[0m")
                                    else:
                                        print("\033[32mSem data Agendada\033[0m")

                        elif opRem1 == "5":
                            for i in adestramento:
                                print(" ")
                                print("\033[31mADESTRAMENTO\033[0m")
                                nomePet = input("Digite o nome do pet:")
                                for pet in pets:
                                    if pet['Nome_Pet'] == nomePet:
                                        while True:
                                            dataAtendimento = input("Digite a nova Data do Adestramento no formato DD/MM/AAAA: ")
                                            if validar_data(dataAtendimento):
                                                break
                                            else:
                                                print("Data inválida. Por favor, digite a data no formato DD/MM/AAAA.")
                                            adesDd['Data_Atendimento'] = dataAtendimento
                                            print("\033[31mData Remarcada\033[0m")
                                    else:
                                        print("\033[32mSem data Agendada\033[0m")

                        elif opRem1 == "6":
                            for i in castracao:
                                print(" ")
                                print("\033[31mCASTRAÇÃO\033[0m")
                                nomePet = input("Digite o nome do pet:")
                                for pet in pets:
                                    if pet['Nome_Pet'] == nomePet:
                                        while True:
                                            dataAtendimento = input("Digite a nova Data da Castração no formato DD/MM/AAAA: ")
                                            if validar_data(dataAtendimento):
                                                break
                                            else:
                                                print("Data inválida. Por favor, digite a data no formato DD/MM/AAAA.")
                                        castDd['Data_Atendimento'] = dataAtendimento
                                        print("\033[31mData Remarcada\033[0m")
                                    else:
                                        print("\033[32mSem data Agendada\033[0m")

                        elif opRem1 == "7":
                            break
            
            elif opcaoaten == "4":
                break

    elif opcao == "3":
        while True:
            opCR = menuConRela()
            if opCR == "1":
                while True:
                    opcaoCon = menuConsu()
                    if opcaoCon == "1":
                        print(" ")
                        print("\033[31mVocê escolheu Consultar Usuário\033[0m")
                        print("\033[31m-------------------------------\033[0m")
                        nome_login = input("Digite o nome de login para consultar: ")
                        for usuario in usuarios:
                            if usuario['Nome_Login'] == nome_login:
                                for chave, valor in usuario.items():
                                    print(f"{chave}: {valor}")
                                break
                            else:
                                print("\033[32mUsuário não encontrado.\033[0m")
        
                    elif opcaoCon == "2":
                        print(" ")
                        print("\033[31mVocê escolheu Consultar Cliente\033[0m")
                        print("\033[31m-------------------------------\033[0m")
                        nome_Cliente = input("Digite o nome do Cliente para consultar: ")
                        for cliente in clientes:
                            if cliente['Nome_Cliente'] == nome_Cliente:
                                for chave, valor in cliente.items():
                                    print(f"{chave}: {valor}")
                                break
                        else:
                            print("\033[32mCliente não encontrado.\033[0m")

                    elif opcaoCon == "3":
                        print(" ")
                        print("\033[31mVocê escolheu Consultar Pet\033[0m")
                        print("\033[31m---------------------------\033[0m")
                        nome_pet = input("Digite o nome do Pet para consultar: ")
                        for pet in pets:
                            if pet['Nome_Pet'] == nome_pet:
                                for chave, valor in pet.items():
                                    print(f"{chave}: {valor}")
                                break
                        else:
                            print("\033[32mPet não encontrado.\033[0m")

                    elif opcaoCon == "4":
                        break
        
            elif opCR == "2":
                while True:
                    opcaoRela = menuRela()
                    if opcaoRela == "1":
                        print(" ")
                        print("\033[31mVocê escolheu Relatório Banhos\033[0m")
                        print("\033[31m------------------------------\033[0m")
                        print(banhos)
                    if opcaoRela == "2":
                        print(" ")
                        print("\033[31mVocê escolheu Relatório Banho e Tosa\033[0m")
                        print("\033[31m------------------------------------\033[0m")
                        print(banhoEtosa)
                    if opcaoRela == "3":
                        print(" ")
                        print("\033[31mVocê escolheu Relatório Tosas\033[0m")
                        print("\033[31m-----------------------------\033[0m")
                        print(tosa)
                    if opcaoRela == "4":
                        print(" ")
                        print("\033[31mVocê escolheu Relatório Consultas Médicas\033[0m")
                        print("\033[31m-----------------------------------------\033[0m")
                        print(consultaMed)
                    if opcaoRela == "5":
                        print(" ")
                        print("\033[31mVocê escolheu Relatório Adestramentos\033[0m")
                        print("\033[31m-------------------------------------\033[0m")
                        print(adestramento)
                    if opcaoRela == "6":
                        print(" ")
                        print("\033[31mVocê escolheu Relatório Castrações\033[0m")
                        print("\033[31m----------------------------------\033[0m")
                        print(castracao)
                    if opcaoRela == "7":
                        print(" ")
                        print("\033[31mVocê escolheu Relatório Atendimentos\033[0m")
                        print("\033[31m------------------------------------\033[0m")
                        print(atendimentos)
                    if opcaoRela == "8":
                        break
                
            elif opCR == "3":
                break

    elif opcao == "4":
        break           

from Classes import *

import os

loja = Loja("VS STORE", "Av. das Codificações, Nº1011", 123456789)
sair = False
menu_adm = 0
menu_cli = 0
admin = Adm("adm", "admin123", 1)

contID = 0

while sair == False:
    try:
        os.system("cls")
        print(" --- BEM VINDO(A) AO VS STORE --- \n")
        print(" [1] - LOGIN ADM")
        print(" [2] - LOGIN CLIENTE")
        print(" [3] - SAIR")

        menu = int(input("\nDigite a opção desejada:  "))
        os.system("cls")
        
        match menu:
            case 1:
                print("--- ADM LOGIN ---")
                user_login = input("Digite o user: ")
                senha_login = input("Digite a senha: ")

                if user_login == admin.user and senha_login == admin.senha:
                    os.system("cls")
                
                    while menu_adm == 0:
                        print("--- MENU DO ADM --- \n")
                        print("[1] - CADASTRAR CLIENTE")
                        print("[2] - CADASTRAR ADM")
                        print("[3] - CADASTRAR PRODUTO")
                        print("[4] - EXCLUIR PRODUTO")
                        print("[5] - EXCLUIR CLIENTE")                     
                        print("[6] - LISTAR CLIENTE")
                        print("[7] - LISTAR PRODUTO")
                        print("[8] - VOLTAR")
                        op_adm = int(input("\nDigite a opção desejada: "))

                        match op_adm:
                            case 1:
                                os.system("cls")
                                contID += 1
                                idc = contID
                                
                                print("--- CADASTRO DE CLIENTE --- \nPreencha as informações:\n")
                                nome = input("NOME: ")
                                cpf = int(input("CPF: "))
                                idade = int(input("IDADE: "))
                                endereco = input("ENDEREÇO: ")
                                senha = input("SENHA: ")

                                admin.cadastrar_cliente(nome, cpf, idade, endereco, senha, idc)

                            case 2:
                                pass
                            case 3:
                                pass
                            case 4:
                                pass
                            case 5:
                                pass
                            case 6:
                                pass
                            case 7:
                                pass
                            case 8:
                                os.system("cls")
                                menu_adm = 1

                            case _:
                                print("Opção inválida.")
                        
                else:
                    print("Credenciais inválidas. Tente novamente.")
            case 2:
                os.system("cls")
                print("--- LOGIN CLIENTE ---")
                cpf_cliente = int(input("Digite o CPF: "))
                senha_cliente = input("Digite a senha: ")

            case 3:  
                print("SAINDO...")
                sair = True
            case _:
                print("Opção inválida.")
                
    except Exception as erro:
            print("Opção inválida.")
            print("Erro:", erro.__class__.__name__)
            os.system("pause")
            os.system("cls")



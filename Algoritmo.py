from Classes import *

import os

loja = Loja("VS STORE", "Av. das Codificações, Nº1011", 123456789)
sair = False
menu_adm = 0
menu_cli = 0
root = Adm("adm", "admin123", 1)
admID = 0

while sair == False:
    try:
        # os.system("cls")
        print(" --- BEM VINDO(A) AO VS STORE --- \n")
        print(" [1] - LOGIN ADM")
        print(" [2] - LOGIN CLIENTE")
        print(" [3] - SAIR")
        menu = int(input("\nDigite a opção desejada: "))
        os.system("cls")
        
        match menu:
            case 1:
        
                print("--- LOGIN ADM ---")
                user_login = input("Digite o user: ")
                senha_login = input("Digite a senha: ")

                id_adm = loja.login_adm(user_login, senha_login)
                if id_adm is not None:
                    while menu_adm == 0: 
                        print("--- MENU ADM --- \n")
                        print("[1] - CADASTRAR CLIENTE")
                        print("[2] - CADASTRAR ADM")
                        print("[3] - CADASTRAR PRODUTO")
                        print("[4] - EXCLUIR PRODUTO")
                        print("[5] - EXCLUIR CLIENTE")                     
                        print("[6] - LISTAR CLIENTE")
                        print("[7] - LISTAR PRODUTO")
                        print("[8] - VOLTAR")
                        op_adm = int(input("\nDigite a opção desejada: "))
                        
                else:
                    print(TypeError)
            case 2:
                os.system("cls")
                print("--- LOGIN CLIENTE ---")
                cpf_cliente = int(input("Digite o CPF: "))
                senha_cliente = input("Digite a senha: ")

                id_cli = root.login_cliente(user_login, senha_login)
                if id_cli is not None:
                    os.system("cls")
                    print(f"Bem-vindo, {Loja.clientes[id_cli].user}!\n")

                    while menu_cli == 0:                
                        print("--- MENU CLIENTE --- \n")
                        print("[1] - ADICIONAR PRODUTO")
                        print("[2] - EXCLUIR PRODUTO")
                        print("[3] - LISTAR PRODUTO")
                        print("[4] - MEU CARRINHO")
                        print("[5] - VOLTAR") 
                        op_cli = int(input("\nDigite a opção desejada: "))               
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


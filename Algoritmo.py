from Classes import *

import os

sair = False
while sair == False:
    try:
        os.system("cls")
        print(" --- BEM VINDO(A) AO  --- ")
        print(" [1] - LOGIN ADM")
        print(" [2] - LOGIN CLIENTE")
        print(" [3] - SAIR")
        menu = int(input("Digite a opção desejada >> "))
        
        match menu:
            case 1:
                
                print("[1] - CADASTRAR CLIENTE")
                print("[2] - CADASTRAR ADM")
                print("[3] - CADASTRAR PRODUTO")
                print("[4] - EXCLUIR PRODUTO")
                print("[5] - EXCLUIR CLIENTE")                     
                print("[6] - LISTAR CLIENTE")
                print("[7] - LISTAR PRODUTO")
            case 2:
                print("[1] - ADICIONAR PRODUTO")
                print("[2] - EXCLUIR PRODUTO")
                print("[3] - LISTAR PRODUTO")
                print("[4] - VER CARRINHO")                
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

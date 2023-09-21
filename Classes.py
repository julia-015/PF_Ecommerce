class Adm:
    def __init__(self, user, senha, id_adm):
        self.user = user
        self.senha = senha
        self.id_adm = id_adm

    def getUser(self):
        return self.user
    
    def getSenha(self):
        return self.senha
    
    def cadastrar_adm(self, user, senha, id_adm):
        adm = ADM(user, senha,id_adm)
        self.adm[id_adm] = adm
        
    def cadastrar_cliente(self, nome, idade, cpf, endereco, senha,id_cli):
        cliente = Cliente(nome, idade, cpf, endereco, senha,id_cli)
        self.clientes[id_cli] = cliente

    def cadastrar_produto(self, nome_produto, descricao, valor):
        produto = Produto(nome_produto, descricao, valor)
        self.produtos[id_pdt] = produto
    
    def estoque(self, produto_id, qtd):
        pass

    def excluir_produto():
        pass

    def excluir_cliente():
        pass

    def excluir_adm():
        pass

    def listar_produto():
        pass
    
    def listar_cliente():
        pass
    
    def listar_adm():
        pass

class Cliente:
    def __init__(self, nome, idade, cpf, endereco, senha):
        self.nome = nome 
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.senha = senha

    def adicionar_produto():
        pass
    def excluir_produto():
        pass
    def meu_carrinho():
        pass

class Produto:
    def __init__(self, nome_produto, descricao, valor):
        self.nome_produto = nome_produto
        self.descricao = descricao
        self.valor = valor

class Carrinho:
    def __init__(self, nome, valor, descricao):
        self.nome = nome
        self.valor = valor
        self.descricao = descricao
        
class Loja:
    def __init__(self, nome, endereco, cnpj):
        self.nome = nome 
        self.endereco = endereco
        self.cnpj = cnpj
        self.adm = {}
        self.clientes = {}
        self.produtos = {}
    
    def login_cliente(self, cpf, senha):
        for id, cliente in self.clientes.items():
            if cpf == cliente.cpf and senha == cliente.senha:
                return id
        return None
    
    def login_adm(self, user_login, senha_login):
        
        for id_adm, adm in self.adm.items():
            if user_login == adm.user and senha_login == adm.senha:
                return id_adm
        return None

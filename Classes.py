class ADM:
    def __init__(self, user, senha):
        self.user = user
        self.senha = senha
    
    def cadastrar_adm(self, user, senha):
        pass
        
    def cadastrar_cliente(self, id, nome, idade, cpf, endereco, senha):
        cliente = Cliente(id, nome, idade, cpf, endereco, senha)
        self.clientes[id] = cliente

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
        

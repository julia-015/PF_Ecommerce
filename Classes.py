class Adm:
    def __init__(self, user, senha, id_adm):
        self.user = user
        self.senha = senha
        self.id_adm = id_adm
    
    def cadastrar_adm(self, user, senha, ida):
        adm = Adm(user, senha, ida)
        loja.inserir_adm(adm, ida)

    def cadastrar_cliente(self, nome, cpf, idade, endereco, senha, idc):
        cliente = Cliente(nome, cpf, idade, endereco, senha, idc)
        loja.inserir_cliente(cliente, idc)

    def cadastrar_produto(self, nome_produto, descricao, valor, idp):
        produto = Produto(nome_produto, descricao, valor, idp)
        loja.inserir_produto(produto, idp)
    
class Cliente:
    def __init__(self, nome, cpf, idade, endereço, senha, idc):
        self.nome = nome 
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereço
        self.senha = senha
        self.id = idc
    
class Produto:
    def __init__(self, nome_produto, descricao, valor, idp):
        self.nome_produto = nome_produto
        self.descricao = descricao
        self.valor = valor
        self.idp = idp
        

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
        self.produtos = {}
        self.clientes = {}
    
    def login_cliente(self, cpf, senha):
        for id, cliente in self.clientes.items():
            if cpf == cliente.cpf and senha == cliente.senha:
                return id
        return None

    def inserir_cliente(self, valor, vetor):
        self.clientes[vetor] = valor
    
    def inserir_produto(self, valor, vetor):
        self.produtos[vetor] = valor

    def inserir_adm(self, valor, vetor):
        self.adm[vetor] = valor


loja = Loja("VS STORE", "Av. das Codificações, Nº1011", 123456789)
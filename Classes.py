class Adm:
    def __init__(self, user, senha, id_adm):
        self.user = user
        self.senha = senha
        self.id_adm = id_adm
        self.clientes = {}
    
    def getUser(self):
        return self.user
    
    def getSenha(self):
        return self.senha
    
    def cadastrar_adm(self, user, senha, id_adm):
        adm = Adm(user, senha, id_adm)
        self.adm[id_adm] = adm

    def cadastrar_cliente(self, nome, cpf, idade, endereco, senha, idc):
        cliente = Cliente(nome, cpf, idade, endereco, senha, idc)
        self.clientes[id] = cliente

    def cadastrar_produto(self, nome_produto, descricao, valor):
        produto = produto (nome_produto, descricao, valor)
        self.produto[a] = produto
    
    def estoque(self, produto_id, qtd):
        estoque = estoque (produto_id,qtd)
        self.estoques = [a]

    def excluir_produto():
        pass

    def excluir_cliente():
        pass

    def excluir_adm():
        pass

    def listar_produto(self):
        for num, produto in self.produtos.items():
            print(f"{num} - Nome: {produto}, Valor: R${Valor}, Descrição: {Descrição}")
    
    def listar_cliente(self):
        for idc, cliente in self.id.items():
            print(f"{num} - Nome: {cliente.user}")
    
    def listar_adm(self):
        for id_adm, adm in self.adm.items(id_adm):
            print(f"{num} - Nome: {adm.user}")

class Cliente:
    def __init__(self, nome, cpf, idade, endereço, senha, idc):
        self.nome = nome 
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereço
        self.senha = senha
        self.id = idc

    def adicionar_produto(self, idc, produto_id, quantidade):
        if idc in self.carrinhos:
                    carrinho = self.carrinhos[idc]
                    if produto_id in self.produtos:
                        produto = self.produtos[produto_id]
                        carrinho.adicionar_produto(produto_id, quantidade)
                    else:
                        print("Produto não encontrado.")
        else:
            print("Carrinho não encontrado.")
            
    def excluir_produto(self, idc, produto_id, quantidade):
        if idc in self.carrinhos:
            carrinho = self.carrinhos[idc]
            if produto_id in self.produtos:
                produto = self.produtos[produto_id]
                carrinho.remover_produto(produto_id, quantidade)
    def meu_carrinho(self, idc):
        if idc in self.carrinhos:
            carrinho = self.carrinhos[idc]
            print("Produtos no carrinho:")
            for produto_num, quantidade in carrinho.produtos.items():
                produto = self.produtos[produto_num]
                print(f"Nome: {nome_produto}, Quantidade: {quantidade}")

class Produto:
    def __init__(self, nome_produto, descricao, valor, quantidade):
        self.nome_produto = nome_produto
        self.descricao = descricao
        self.valor = valor
        self.quantidade = quantidade

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
        
    
    def login_cliente(self, cpf, senha):
        for id, cliente in self.clientes.items():
            if cpf == cliente.cpf and senha == cliente.senha:
                return id
        return None
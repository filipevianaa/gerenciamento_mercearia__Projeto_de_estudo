from datetime import datetime

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Produtos:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produtos, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Vendas:
    def __init__(self, item_vendido: Produtos, vendedor, comprador, quantidade_vendida, data = datetime.now()):
        self.item_vendido = item_vendido
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidade_vendida = quantidade_vendida
        self.data = data

class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria

class Pessoa:
    def __init__(self, nome, telefone, cpf, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

class Funcionario(Pessoa):
    def __init__(self, clt, nome, telefone, cpf, email, endereco):
        self.clt = clt
        super(Funcionario, self).__init__(nome, telefone, cpf, email, endereco)
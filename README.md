# gerenciamento_mercearia__Projeto_de_estudo

## Aplicação para gerenciamento de uma mercearia de pequeno porte ##

A aplicação está sendo desenvolvida seguindo a metodologia de projeto MVC (Model, View e Controller)

# MODEL #
o model consta com as classes:
    Categoria: Que recebe apenas um parâmetro
    Produto: recebe os parâmetros 'nome', 'preco' e 'categoria '
    Estoque: Recebe os parâmetros de Produto e 'quantidade'
    Venda: Recebe os parâmetros de Produto, 'vendedor', 'comprador', 'quantidade_vendida' e 'data'
    Fornecedor: Recebe 'nome', 'cnpj', 'telefone' e 'categoria'
    Pessoa: recebe 'nome', 'telefone', 'cpf', 'email' e 'endereco'
    Funcionário herda parâmetros de Pessoa e recebe 'clt'

# DAO #
Os dados estão sendo armazenados em um arquivo .txt gerados no arquivo DAO.py com métodos de classe para salvar e para ler as linhas de dados e retorná-los em uma lista 

# CONTROLLER #

O controller é onde são determinadas as "regras de negócio"

O Controller da Categoria (CategoriaController) possui um método para cadastrar uma nova categoria com validação para impedir categorias duplicadas, outro método para remover uma categoria com checagem se aquela categoria realmente existe, um método para alterar o nome de uma categoria já existente e um método para exibir a lista de categorias cadastradas.

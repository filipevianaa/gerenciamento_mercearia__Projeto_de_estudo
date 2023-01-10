import controller
import os.path

if __name__ == '__main__':
    while True:
        local = int(input("Digite 1 para acessar ( Categorias )\n"
                            "Digite 2 para acessar ( Estoque )\n"
                            "Digite 3 para acessar ( Fornecedor )\n"
                            "Digite 4 para acessar ( Cliente )\n"
                            "Digite 5 para acessar ( Funcionario )\n"
                            "Digite 6 para acessar ( Vendas )\n"
                            "Digite 7 para ver os produtos mais vendidos\n"
                            "Digite 8 para sair\n"))

        if local == 1:
            cat = controller.CategoriaController()
            while True:
                decidir = int(input("Digite 1 para cadastrar    uma categoria\n"
                                    "Digite 2 para remover uma categoria\n"
                                    "Digite 3 para alterar uma categoria\n"
                                    "Digite 4 para mostrar as categorias cadastradas\n"
                                    "Digite 5 para sair\n"))

                if decidir == 1:
                    categoria = input('Digite a categoria que deseja cadastrar \n')

                    cat.cadastra_categoria(categoria)

                elif decidir == 2:
                    categoria = input('Digite a categoria que deseja remover \n')

                    cat.remove_categoria(categoria)

                elif decidir == 3:
                    categoria = input('Digite a categoria que deseja alterar \n')

                    categoria_novo = input('Digite a categoria para a qual deseja alterar \n')

                    cat.alterar_categoria(categoria, categoria_novo)

                elif decidir == 4:
                    cat.mostrar_categoria()
                
                else:
                    break

        elif local == 2:
            est = controller.EstoqueController()

            while True:
                decidir = int(input("Digite 1 para cadastrar um produto\n"
                                    "Digite 2 para remover um produto\n"
                                    "Digite 3 para alterar um produto\n"
                                    "Digite 4 para ver o estoque\n"
                                    "Digite 5 para sair\n"))

                if decidir == 1:
                    nome = input('Digite o nome do produto')
                    preco = input('Digite o preço do produto')
                    categoria = input('Digite a categoria do produto')
                    quantidade = input('Digite a quantidade do produto')

                    est.cadastra_categoria(nome, preco, categoria, quantidade)

                elif decidir == 2:
                    produto = input('Digite o produto que deseja remover')

                    est.remover_produto(produto)

                elif decidir == 3:

                    nome_antigo = input('Digite o nome do produto que deseja alterar')
                    nome_novo = input('Digite o novo nome do produto')
                    preco = input('Digite o novo preço do produto')
                    categoria = input('Digite a nova categoria do produto')
                    quantidade = input('Digite a nova quantidade do produto')

                    est.alterar_produto(nome_antigo, nome_novo, preco, categoria, quantidade)

                elif decidir == 4:
                    est.mostrar_estoque()

        elif local == 3:
            forn = controller.FornecedorController()

            while True:
                decidir = int(input("Digite 1 para cadastrar um fornecedor\n"
                                    "Digite 2 para remover um fornecedor\n"
                                    "Digite 3 para alterar um fornecedor\n"
                                    "Digite 4 para mostrar fornecedores\n"
                                    "Digite 5 para sair"))

                if decidir == 1:
                    nome = input("Digite o nome do fornecedor: \n")
                    cnpj = input("Digite o cnpj do fornecedor: \n")
                    telefone = input("Digite o telefone do fornecedor: \n")
                    categoria = input("Digite a categoria fornecida: \n")
                    forn.cadastrar_fornecedor(nome, cnpj, telefone, categoria)

                elif decidir == 2:
                    fornecedor = input("Digite o fornecedor que deseja remover: \n")
                    forn.remover_fornecedor(fornecedor)

                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do fornecedor que deseja alterar: \n")
                    novoNome = input('Digite o novo nome do fornecedor: \n')
                    novoCnpj = input('Digite o novo cnpj do fornecedor: \n')
                    novoTelefone = input('Digite o novo telefone do fornecedor: \n')
                    novoCategoria = input('Digite a nova categoria fornecida: \n')

                    forn.alterar_fornecedor(nomeAlterar, novoNome, novoCnpj, novoTelefone, novoCategoria)

                elif decidir == 4:
                    forn.mostrar_fornecedor()

                else:
                    break

        elif local == 4:
            cat = controller.ClienteController()

            while True:
                decidir = int(input("Digite 1 para cadastrar um cliente\n"
                                    "Digite 2 para remover um cliente\n"
                                    "Digite 3 para alterar um cliente\n"
                                    "Digite 4 para mostrar clientes\n"
                                    "Digite 5 para sair\n"))

                if decidir == 1:
                    nome = input("Digite o nome do cliente: \n")
                    telefone = input("Digite o telefone do cliente: \n")
                    cpf = input("Digite o cpf do cliente: \n")
                    email = input("Digite o email do cliente: \n")
                    endereco = input("Digite o endereço do cliente: \n")

                    cat.cadastrar_cliente(nome, telefone, cpf, email, endereco)

                elif decidir == 2:
                    cliente = input("Digite o cliente que deseja remover: \n")

                    cat.remover_cliente(cliente)

                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do cliente que deseja alterar: \n")
                    novoNome = input("Digite o novo nome do cliente: \n")
                    novoTelefone = input("Digite o novo telefone do cliente: \n")
                    novoCpf = input("Digite o novo cpf do cliente: \n")
                    novoEmail = input("Digite o novo email do cliente: \n")
                    novoEndereco = input("Digite o novo endereço do cliente: \n")
                    cat.alterar_cliente(nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)

                elif decidir == 4:
                    cat.mostrar_cliente()

                else:
                    break

        elif local == 5:
            cat = controller.FuncionarioController()

            while True:
                decidir = int(input("Digite 1 para cadastrar um funcionario\n"
                                    "Digite 2 para remover um funcionario\n"
                                    "Digite 3 para alterar um funcionario\n"
                                    "Digite 4 para mostrar funciorios\n"
                                    "Digite 5 para sair\n"))

                if decidir == 1:
                    clt = input("Digite a clt do funcionario: \n")
                    nome = input("Digite o nome do funcionario: \n")
                    telefone = input("Digite o telefone do funcionario: \n")
                    cpf = input("Digite o cpf do funcionario: \n")
                    email = input("Digite o email do funcionario: \n")
                    endereco = input("Digite o endereço do funcionario: \n")

                    cat.cadastrar_funcionario(clt, nome, telefone, cpf, email, endereco)

                elif decidir == 2:                    
                    funcionario = input("Digite o funcionario que deseja remover: \n")
                    cat.remover_funcionario(funcionario)

                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do funcionario que deseja alterar: \n")
                    novoClt = input("Digite a nova clt do funcionario: \n")
                    novoNome = input("Digite o novo nome do funcionario: \n")
                    novoTelefone = input("Digite o novo telefone do funcionario: \n")
                    novoCpf = input("Digite o novo cpf do funcionario: \n")
                    novoEmail = input("Digite o novo email do funcionario: \n")
                    novoEndereco = input("Digite o novo endereço do funcionario: \n")
                    cat.alterar_funcionario(nomeAlterar, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)

                elif decidir == 4:
                    cat.mostrar_funcionario()

                else:
                    break

        elif local == 6:
            cat = controller.VendaController()

            while True:
                decidir = int(input("Digite 1 para realizar uma venda\n"
                                    "Digite 2 para ver as vendas\n"
                                    "Digite 3 para sair\n"))

                if decidir == 1:
                    nome = input('Digite o nome do produto: \n')
                    vendedor = input('Digite nome do vendedor: \n')
                    comprador = input('Digite o nome do cliente: \n')
                    quantidade = input('Digite a quantidade: \n')
                    cat.cadastrar_venda(nome, vendedor, comprador, quantidade)

                elif decidir == 2:
                    dataInicio = input("Digite a data de inicio no formato dia/mes/ano: \n")
                    dataTermino = input("Digite a data de termino no formato dia/mes/ano: \n")
                    cat.mostrar_venda(dataInicio, dataTermino)

        elif local == 7:
            cat = controller.VendaController()
            cat.relatorio_produtos()

        else:
            break
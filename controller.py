from model import Categoria, Produto, Estoque, Venda, Fornecedor, Pessoa, Funcionario
from DAO import CategoriaDao, ProdutoDao, EstoqueDao, VendaDao, PessoaDao, FuncionarioDao, FornecedorDao
from datetime import datetime

class CategoriaController:
    def cadastra_categoria(self, nova_categoria):
        existe = False
        x = CategoriaDao.ler()
        for i in x:
            if i.categoria == nova_categoria:
                existe = True

        if not existe:
            CategoriaDao.salvar(nova_categoria)
            print(f'Categoria {nova_categoria} cadastrada com sucesso')
        else:
            print(f'A categoria {nova_categoria} já existe')

    def remove_categoria(self, categoria_removida):
        x = CategoriaDao.ler()
        
        cat = list(filter(lambda x: x.categoria == categoria_removida, x))
        if len(cat) <= 0:
            print('A categoria que deseja remover não existe')
        else:
            for i in range(len(x)):                
                if x[i].categoria == categoria_removida:
                    del x[i]
                    break

            print(f'Categoria {categoria_removida} removida com sucesso')

            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

    def alterar_categoria(self, categoria_antiga, categoria_alterada):
        x = CategoriaDao.ler()

        cat = list(filter(lambda x: x.categoria == categoria_antiga, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoria_alterada, x))

            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoria_alterada) if(x.categoria == categoria_antiga) else(x), x))
                print(f'A categoria {categoria_antiga} foi alterada para {categoria_alterada}')

            else:
                print('Já existe uma categoria com esse nome')


        else:
            print('A categoria que você deseja alterar não existe')

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrar_categoria(self):
        x = CategoriaDao.ler()

        if len(x) == 0:
            print('Não existem categorias cadastradas')
        else:
            for i in x:
                print(i.categoria)

class EstoqueController:
    def cadastrar_produto(self, nome, preco, categoria, quantidade):
        x = EstoqueDao.ler()
        y = CategoriaDao.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produto(nome, preco, categoria)
                EstoqueDao.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso')
            else:
                print('Produto já existe em estoque')
        else:
            print('Categoria inexistente')

    def remover_produto(self, nome):
        x = EstoqueDao.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    print('Produto removido com sucesso')
                    break
        else:
            print('O produto que deseja remover não existe')

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome +'|'+ i.produto.preco +'|'+ i.produto.categoria +'|'+ i.quantidade)
                arq.writelines('\n')

    def alterar_produto(self, nome_antigo, nome_novo, preco_novo, categoria_novo, quantidade_novo):
        x = EstoqueDao.ler()
        y = CategoriaDao.ler()
        h = list(filter(lambda x: x.categoria == categoria_novo, y))
        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nome_antigo, x))

            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == nome_novo, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produto(nome_novo, preco_novo, categoria_novo), quantidade_novo) if (x.produto.nome == nome_antigo) else(x), x))
                    print('Produto alterado com sucesso')
                else:
                    print('Produto já cadastrado')
            else:
                print('O produto que deseja alterar não existe')

            with open('estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome +'|'+ i.produto.preco +'|'+ i.produto.categoria +'|'+ i.quantidade)
                    arq.writelines('\n')
        else:
            print('A categoria informada não existe')

    def mostrar_estoque(self):
        estoque = EstoqueDao.ler()

        if len(estoque) == 0:
            print('Estoque vazio')
        else:
            print('==========Produtos==========')
            for i in estoque:
                print(f'Nome: {i.produto.nome} \n'
                        f'Categoria: {i.produto.categoria} \n'
                        f'Preço: {i.produto.preco} \n'
                        f'Quantidade: {i.quantidade}')

                print('--------------------------')

class VendaController:
    def cadastrar_venda(self, nome_produto, vendedor, comprador, quantidade_vendida):
        x = EstoqueDao.ler()
        temp = []
        existe = False
        qtd = False

        for i in x:
            if existe == False:
                if i.produto.nome == nome_produto:
                    existe = True
                    if int(i.quantidade) >= quantidade_vendida:
                        qtd = True
                        i.quantidade = int(i.quantidade) - int(quantidade_vendida)

                        vendido = Venda(Produto(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidade_vendida)

                        valor_da_compra = int(quantidade_vendida) * int(i.produto.preco)

                        VendaDao.salvar(vendido)

            temp.append([Produto(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])

            with open('estoque.txt', 'w') as arq:
                for i in temp:
                    arq.writelines(i[0].nome +'|'+ i[0].preco +'|'+ i[0].categoria +'|'+ str(i[1]))
                    arq.writelines('\n')


        if existe == False:
            print('O produto não existe')
            return None
        elif not qtd:
            print('A quantidade vendida não contém em estoque')
        else:
            print('Venda realizada com suecesso')
            return valor_da_compra

    def relatorio_produtos(self):
        vendas = VendaDao.ler()
        produtos = []

        for i in vendas:
            nome = i.item_vendido.nome
            quantidade = int(i.quantidade_vendida)
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, "quantidade": int(x['quantidade']) + int(quantidade)} if(x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': quantidade})


            ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)

        print('Esses são os produtos mais vendidos: ')
        for i in ordenado:
            print(f'Produto: {i["produto"]}  | Quantidade:  {i["quantidade"]}')


    def mostrar_venda(self, data_inicio, data_termino):
        vendas = VendaDao.ler()
        data_inicio1 = datetime.strptime(data_inicio, '%d/%m/%Y')
        data_termino1 = datetime.strptime(data_termino, '%d/%m/%Y')

        vendas_selecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= data_inicio1 and datetime.strptime(x.data, '%d/%m/%Y') <= data_termino1, vendas))

        cont = 1
        total = 0

        print(f'### VENDAS no período de {data_inicio1} a {data_termino1} ###')
        for i in vendas_selecionadas:
            print(f'-------- VENDA {cont} -------- \n Nome: {i.item_vendido.nome} \n Categoria: {i.item_vendido.categoria} \n Data: {i.data} \n Quantidade: {i.quantidade_vendida} \n Preço unitário: {i.item_vendido.preco} \n Cliente: {i.comprador} \n Vendedor: {i.vendedor}')

            cont += 1
            total += int(i.item_vendido.preco) * int(i.quantidade_vendida)

        print(f'O total vendido foi de R$ {total}')

class FornecedorController:
    def cadastrar_fornecedor(self, nome, cnpj, telefone, categoria):
        x = FornecedorDao.ler()

        lista_cnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        lista_telefone = list(filter(lambda x: x.telefone == telefone, x))

        if len(lista_cnpj) > 0:
            print('O CNPJ já existe')
        elif len(lista_telefone) > 0:
            print('O telefone já existe')
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                FornecedorDao.salvar(Fornecedor(nome, cnpj, telefone, categoria))
                print('Fornecedor cadastrado com sucesso')
            else:
                print('Digite um CNPJ ou telefone válido')

    def alterar_fornecedor(self, nome_antigo, nome_novo, cnpj_novo, telefone_novo, categoria_novo):        
        x = FornecedorDao.ler()

        est = list(filter(lambda x: x.nome == nome_antigo, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.cnpj == cnpj_novo, x))
            if len(est) == 0:
                x = list(map(lambda x: Fornecedor(nome_novo, cnpj_novo, telefone_novo, categoria_novo) if(x.nome == nome_antigo) else(x), x))
                print('fornecedor alterado com sucesso!')
            else:
                print('CNPJ já existe')

        else:
            print('O fornecedor que deseja alterar não existe')

        with open('fornecedor.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome +'|'+ i.cnpj +'|'+ i.telefone +'|'+ str(i.categoria))
                arq.writelines('\n')
            
            

    def remover_fornecedor(self, nome):
        x = FornecedorDao.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('O fornecedor que deseja remover não existe')
            return None

        with open('fornecedor.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome +'|'+ i.cnpj +'|'+ i.telefone +'|'+ str(i.categoria))
                arq.writelines('\n')

            print('Fornecedor removido com sucesso')

    def mostrar_fornecedor(self):
        fornecedores = FornecedorDao.ler()

        if len(fornecedores) == 0:
            print('Lista de fornecedores vazia')
        
        for i in fornecedores:
            print('============= FORNECEDOR ===========')
            print(f'Categoria fornecida: {i.categoria} \n Nome: {i.nome} \n Telefone {i.telefone} \n CNPJ: {i.cnpj}')

class ClienteController:
    def cadastrar_cliente(self, nome, telefone, cpf, email, endereco):
        x = PessoaDao.ler()

        lista_cpf = list(filter(lambda x: x.cpf == cpf, x))

        if len(lista_cpf) > 0:
            print('CPF já existe')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                PessoaDao.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print('Cliente cadastrado com sucesso!')
            else:
                print('Digite um cpf ou telefone válido')

    def alterar_cliente(self, nome_antigo, nome_novo, cpf_novo, telefone_novo, email_novo, endereco_novo):
        x = PessoaDao.ler()

        est = list(filter(lambda x: x.nome == nome_antigo, x))
        if len(est) > 0:
            x = list(map(lambda x: Pessoa(nome_novo, telefone_novo, cpf_novo, email_novo, endereco_novo) if(x.nome == nome_antigo) else(x), x))
            print('cliente alterado com sucesso')
        else:
            print('O cliente que deseja alterar não existe')

        with open('cliente.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome +'|'+ i.telefone +'|'+ i.cpf +'|'+ i.email +'|'+ i.endereco)
                arq.writelines('\n')

    def remover_cliente(self, nome):
        x = PessoaDao.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    print('cliente removido com sucesso')
                    break

        else:
            print('O cliente que deseja remover não existe')
            return None

        with open ('cliente.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome +'|'+ i.telefone +'|'+ i.cpf +'|'+ i.email +'|'+ i.endereco)
                arq.writelines('\n')

    def mostrar_cliente(self):
        clientes = PessoaDao.ler()

        if len(clientes) == 0:
            print('Lista de clientes vazia')

        for i in clientes:
            print('=========== CLIENTE ============')
            print(f'Nome: {i.nome} \n Telefone: {i.telefone} \n Endereco: {i.endereco} \n Email: {i.email} \n CPF: {i.cpf}')

class FuncionarioController:
    def cadastrar_funcionario(self, clt, nome, telefone, cpf, email, endereco):
        x = FuncionarioDao.ler()

        lista_cpf = list(filter(lambda x: x.cpf == cpf, x))
        lista_clt = list(filter(lambda x: x.clt == clt, x))

        if len(lista_cpf) > 0:
            print('CPF já existente')
        elif len(lista_clt) > 0:
            print('Já existe um funcionário com essa CLT')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len (telefone) <= 11:
                FuncionarioDao.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print('Funcionário cadastrado com sucesso')

            else:
                print('Digite um CPF ou telefone válido')

    def alterar_funcionario(self, nome_antigo, clt_novo, nome_novo, telefone_novo, cpf_novo, email_novo, endereco_novo):
        x = FuncionarioDao.ler()

        est = list(filter(lambda x: x.nome == nome_antigo, x))
        if len(est) > 0:
            x = list(map(lambda x: Funcionario(clt_novo, nome_novo, telefone_novo, cpf_novo, email_novo, endereco_novo) if(x.nome == nome_antigo) else(x), x))
            print('Funcionário alterado com sucesso')
        else:
            print('O funcionário que deseja alterar não existe')

        with open ('funcionario.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.clt +'|'+ i.nome +'|'+ i.telefone +'|'+ i.cpf +'|'+ i.email)
                arq.writelines('\n')

    def remover_funcionario(self, nome):
        x = FuncionarioDao.ler()

        est = list(filter(lambda x: x.nome == nome, x))


        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    print('Funcionário removido com sucesso')
                    break
        else:
            print('O funcionário que deseja remover não existe')
            return None

        with open ('funcionario.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')

    def mostrar_funcionario(self):
        funcionario = FuncionarioDao.ler()

        if len(funcionario) == 0:
            print('Lista de funcionários vazia')

        for i in funcionario:
            print('========== FUNCIONÁRIO ==========')
            print(f"Nome: {i.nome}\n"
                f"Telefone: {i.telefone}\n"
                f"Email: {i.email}\n"
                f"Endereço: {i.endereco}\n"
                f"CPF: {i.cpf}\n"
                f"CLT: {i.clt}\n")



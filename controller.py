from model import Categoria, Produto, Estoque, Venda, Fornecedor, Pessoa, Funcionario
from DAO import CategoriaDao, ProdutoDao, EstoqueDao, VendaDao, PessoaDao, FuncionarioDao
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
            quantidade = i.quantidade_vendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, "quantidade": quantidade + x['quantidade']} if(x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': quantidade})


            ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)

            print('Esses são os produtos mais vendidos: ')
            for i in ordenado:
                print('Produto: ' + i['produto'] + ' Quantidade: '+ i['quantidade'])







# a = EstoqueController()
# a.cadastrar_produto(nome, preco, categoria, quantidade)
# a.cadastrar_produto('Melao', '20', "Frutas", '200')
# a.cadastrar_produto('Cereja', '5', 'Frutas', '500')
# a.cadastrar_produto('Ameixa', '20', 'Frutas', '200')
# a.cadastrar_produto('Laranja', '10', 'Frutas', '100')

a = VendaController()

# a.cadastrar_venda('Laranja', 'Filipe', 'Jefs', 2)

a.relatorio_produtos()
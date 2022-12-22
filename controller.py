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
        h = list(filter(lambda x: x.categoria == categoria, x))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produto(nome, preco, categoria)
                
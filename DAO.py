from model import Categoria, Produtos, Estoque, Vendas, Fornecedor, Pessoa, Funcionario


class CategoriaDao:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        print(cls.categoria)


CategoriaDao.salvar("Frutas")
CategoriaDao.salvar("Legumes")
CategoriaDao.salvar("Verguras")

CategoriaDao.ler()
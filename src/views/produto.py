from ..dao.produto_dao import ProdutoDao as dao
from ..models.item_model import ItemModel
from ..models.produto_model import ProdutoModel
from ..utils.utils import Utils
from ..styles.cores import Cores as cor


class Produto():

    @staticmethod
    def cadastro(nome='', preco='', exibe_cabecalho=True):
        if exibe_cabecalho:
            Utils.titulo("Cadastro de Produto")
        try:

            nome, preco = Produto.__validar_nomes()
            produto = ProdutoModel()
            produto.nome = nome
            produto.preco = preco

            dao.inserir(produto)
            Utils.limpar_tela()
            Utils.messagem_success("Inserido com sucesso")

            while True:
                print("Deseja cadastar novo produto?")
                print("1 - Sim")
                print("2 - Não")
                print("0 - Retornar ao menu anterior")
                opcao_selecionado = Utils.obtem_opcao_menu(1, 2)
                if opcao_selecionado == 1:
                    Utils.limpar_tela()
                    nome = ""
                    preco = ""
                    Produto.cadastro(
                        nome, preco, exibe_cabecalho=True,)
                if opcao_selecionado == 2 or opcao_selecionado == 0:
                    Utils.limpar_tela()
                    break

        except Exception as e:
            Utils.messagem_error(e=e)
            return Produto.cadastro(nome, preco, exibe_cabecalho=False)

    @staticmethod
    def listar():
        produtos = dao.listar()
        Utils.limpar_tela()
        Utils.titulo("Relatório de Produtos")
        for produto in produtos:
            print(f"\ncodigo: {produto.codigo}")
            print(f"Nome: {produto.nome}")
            print(f"Preço: {produto.preco}")
            print(f"{cor.CTEXTINFO}{'-' * 30}{cor.CEND}")

        input("Digite enter para sair do relatório \n")
        Utils.limpar_tela()

    @staticmethod
    def adicionar_carrinho(produto="", quantidade="", itens=[]):
        try:
            produtos = dao.listar()
            Utils.titulo("Adicionar item")
            itens = itens
            print(f"CÓDIGO | Descrição | Preço")
            for produto in produtos:
                print(f"{produto.codigo} - {produto.nome} R$ {produto.preco}")

            opcao_selecionada = Utils.obtem_opcao_menu(1, len(produtos))

            objeto_produto = dao.busca_por_id(opcao_selecionada)
            produto = objeto_produto.nome
            valor_produto = objeto_produto.preco
            if produto.strip() == "":
                raise TypeError("Digite o produto correto.")
            if quantidade.strip() == "":
                quantidade = Utils.obter_numero(
                    f"Digite a quantidade de [{produto.strip()}]")

            item = ItemModel(produto=produto, preco=float(
                valor_produto), qtd=quantidade)
            itens.append(item)

            while True:
                Utils.limpar_tela()
                Utils.titulo("Deseja cadastar novo produto?")
                print("1 - Sim")
                print("0 - Não")
                opcao_selecionado = Utils.obtem_opcao_menu(1, 1)
                if opcao_selecionado == 0:
                    Utils.limpar_tela()
                    return itens
                elif opcao_selecionado == 1:
                    Utils.limpar_tela()
                    produto = ""
                    quantidade = ""
                    Produto.adicionar_carrinho(
                        produto, quantidade)

        except Exception as e:
            Utils.messagem_error(e=e)
            return Produto.adicionar_carrinho(produto, quantidade, itens)

    def __validar_nomes(nome='', preco=''):
        try:
            if nome.strip() == "":
                nome = input("Digite o nome:")
                if nome.strip() == "":
                    raise TypeError("Digite o nome correto.")

            if not Utils.number_float(preco) or preco.strip() == "":
                preco = input("Digite o preço:")
                if not Utils.number_float(preco):
                    raise TypeError("Digite o preço correto.")

            return nome, preco
        except Exception as e:
            Utils.messagem_error(e=e)
            return Produto.__validar_nomes(nome, preco)

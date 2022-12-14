from ..utils.utils import Utils
from ..models.pedido_model import PedidoModel
from ..styles.cores import Cores as cor
from ..dao.pedido_dao import PedidoDao as dao


class Pedido():

    @staticmethod
    def cadastro(id_cliente, items=[], exibe_cabecalho=False):
        if exibe_cabecalho:
            Utils.titulo("Novo Pedido")
        try:

            valor_total = Pedido.__calcular_total_venda(items)

            novo_pedido = PedidoModel()
            novo_pedido.adicionar_id_cliente(id_cliente)
            novo_pedido.adicionar_produto(items)

            novo_pedido.valor_total = valor_total
            
            dao.inserir(novo_pedido)
            Utils.limpar_tela()
            Utils.messagem_success("Inserido com sucesso")

        except Exception as e:
            Utils.messagem_error(e=e)

    @staticmethod
    def listar():
        pedidos = dao.listar()
        Utils.limpar_tela()
        Utils.titulo("Relatório de Pedidos")
        for pedido in pedidos:
            print(f"\ncodigo: {pedido.id}")
            print(f"Nome: {pedido.nome}")
            print(f"Email: {pedido.email}")
            print(f"{cor.CTEXTINFO}{'-' * 30}{cor.CEND}")
            print(f"#|Descrição|Qtde|Volor unit.|Valor total")
            print(f"{cor.CTEXTINFO}{'-' * 30}{cor.CEND}")
            itens_total = []
            i = 1
            for item in pedido.itens:
                itens_total.append(item.preco * item.qtd)
                print(
                    f"{i} {item.produto} {item.qtd} unid  x {item.preco} {item.qtd * item.preco}")
                i += 1
            print(f"Valor Total R$ {sum(itens_total)}")
            print(f"{cor.CTEXTINFO}{'-' * 30}{cor.CEND}")

        input("Digite enter para sair do relatório \n")
        Utils.limpar_tela()

    def __calcular_total_venda(items=[]):
        valor_total = 0

        if len(items) > 0:
            for item in items:
                valor_total += item.qtd * item.preco

            return valor_total

        return valor_total

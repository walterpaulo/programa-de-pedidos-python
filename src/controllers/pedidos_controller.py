from ..controllers.clientes_controller import ClientesController
from ..controllers.produtos_controller import ProdutosController
from ..views.pedido import Pedido
from ..utils.utils import Utils


class PedidosController():
    def exec():

        Utils.titulo("Novo Pedido")
        id_cliente = ClientesController.cadastrar_cliente_pedido()
        itens = ProdutosController.adicionar_produto()

        Pedido.cadastro(id_cliente, itens)

    def relatorio():
        Pedido.listar()


if __name__ == "__main__":
    PedidosController.exec()

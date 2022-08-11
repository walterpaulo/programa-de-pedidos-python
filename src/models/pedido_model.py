import json
import os
import uuid
from ..utils.utils import Utils
from ..models.cliente_model import ClienteModel
from ..models.item_model import ItemModel


class PedidoModel():
    def __init__(self, id=""):
        self.id = id
        self.itens = []
        self.id_cliente = int

    def adicionar_id_cliente(self,id):
        self.id_cliente = id

    def adicionar_produto(self, list_produto):
        lista_objeto = []
        for produto in list_produto:
            objeto = ItemModel(
                produto=produto.produto, preco=produto.preco, qtd=produto.qtd)
            lista_objeto.append(objeto)

        self.itens = lista_objeto

    def converter_dict_obj_produto(self, list_dict_produto):
        lista_objeto = []
        for produto in list_dict_produto:
            objeto = ItemModel(
                produto=produto["produto"], preco=produto["preco"], qtd=produto["qtd"])
            lista_objeto.append(objeto)

        return lista_objeto

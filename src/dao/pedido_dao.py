from ..config.conexao import Conexao
from ..utils.utils import Utils
from ..dao.dto.pedido_dto import PedidoDto


class PedidoDao():
    def inserir(pedido=object):
        try:
            lista_json = Utils.objecto_to_json(pedido.itens)
            sql = f"INSERT INTO pedidos (id_cliente, itens) VALUES ({pedido.id_cliente},'{lista_json}')"
            conn = Conexao.conectar()
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            Conexao.fechar_conexao(conn)
        except TypeError as e:
            Utils.messagem_error(e=e)
            Conexao.fechar_conexao(conn)
        Conexao.fechar_conexao(conn)

    def listar():
        try:
            sql = "select pedidos.id, clientes.nome, clientes.email, pedidos.itens from pedidos inner join clientes on pedidos.id_cliente = clientes.id"
            conn = Conexao.conectar()
            cur = conn.cursor()
            cur.execute(sql)
            recset = cur.fetchall()
            registros = []
            for rec in recset:
                lista_itens = Utils.string_to_objeto_item(rec[3])
                objeto = PedidoDto(id=rec[0], nome=rec[1], email=rec[2], itens=lista_itens)

                registros.append(objeto)
            Conexao.fechar_conexao(conn)
            return registros
        except TypeError as e:
            Utils.messagem_error(e=e)
            Conexao.fechar_conexao(conn)
        Conexao.fechar_conexao(conn)

    def busca_por_id(id):
        try:
            sql = "select * from pedidos where id = %s"
            conn = Conexao.conectar()
            cur = conn.cursor()
            cur.execute(sql, (id))
            recset = cur.fetchall()
            registros = []
            for rec in recset:
                registros.append(rec)
            Conexao.fechar_conexao(conn)
            return registros
        except TypeError as e:
            Utils.messagem_error(e=e)
            Conexao.fechar_conexao(conn)
        Conexao.fechar_conexao(conn)

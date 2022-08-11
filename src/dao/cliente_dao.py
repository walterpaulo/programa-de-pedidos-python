from ..config.conexao import Conexao
from ..models.cliente_model import ClienteModel
from ..utils.utils import Utils


class ClienteDao():
    def inserir(nome, email):
        try:
            sql = "INSERT INTO clientes (nome, email) VALUES (%s,%s) RETURNING id;"
            conn = Conexao.conectar()
            cur = conn.cursor()
            cur.execute(sql, (nome, email))
            conn.commit()
            id_linha = cur.fetchone()[0]
            Conexao.fechar_conexao(conn)
            return id_linha
        except TypeError as e:
            Utils.messagem_error(e=e)
            Conexao.fechar_conexao(conn)
        Conexao.fechar_conexao(conn)

    def listar():
        try:
            sql = "select * from clientes"
            conn = Conexao.conectar()
            cur = conn.cursor()
            cur.execute(sql)
            recset = cur.fetchall()
            registros = []
            for rec in recset:
                objeto_cliente = ClienteModel(
                    id=rec[0], nome=rec[1], email=rec[2])
                registros.append(objeto_cliente)
            Conexao.fechar_conexao(conn)
            return registros
        except TypeError as e:
            Utils.messagem_error(e=e)
            Conexao.fechar_conexao(conn)
        Conexao.fechar_conexao(conn)

    def busca_por_id(id):
        try:
            sql = "select * from clientes where id = %s"
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

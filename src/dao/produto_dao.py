from ..config.conexao import Conexao
from ..models.produto_model import ProdutoModel
from ..utils.utils import Utils


class ProdutoDao():
    def inserir(produto=object):
        try:
            sql = "INSERT INTO produtos (nome, preco) VALUES (%s,%s)"
            conn = Conexao.conectar()
            cur = conn.cursor()
            cur.execute(sql, (produto.nome, produto.preco))
            conn.commit()
            Conexao.fechar_conexao(conn)
        except TypeError as e:
            Utils.messagem_error(e=e)
            Conexao.fechar_conexao(conn)
        Conexao.fechar_conexao(conn)

    def listar():
        try:
            sql = "select * from produtos"
            conn = Conexao.conectar()
            cur = conn.cursor()
            cur.execute(sql)
            recset = cur.fetchall()
            registros = []
            for rec in recset:
                objeto_produto = ProdutoModel(
                    codigo=rec[0], nome=rec[1], preco=rec[2])
                registros.append(objeto_produto)
            Conexao.fechar_conexao(conn)
            return registros
        except TypeError as e:
            Utils.messagem_error(e=e)
            Conexao.fechar_conexao(conn)
        Conexao.fechar_conexao(conn)

    def busca_por_id(id):
        try:
            sql = f"select * from produtos where id = {id}"
            conn = Conexao.conectar()
            cur = conn.cursor()
            cur.execute(sql)
            produto = cur.fetchone()
            objeto_produto = ProdutoModel(
                codigo=produto[0], nome=produto[1], preco=produto[2])
            Conexao.fechar_conexao(conn)
            return objeto_produto
        except TypeError as e:
            Utils.messagem_error(e=e)
            Conexao.fechar_conexao(conn)
        Conexao.fechar_conexao(conn)

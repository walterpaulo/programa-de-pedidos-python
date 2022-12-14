from ..utils.utils import Utils
from ..models.cliente_model import ClienteModel
from ..styles.cores import Cores as cor
from ..dao.cliente_dao import ClienteDao as dao


class Cliente():

    @staticmethod
    def cadastro(nome='', email='', exibe_cabecalho=True, cadastro_pedido=False):
        if exibe_cabecalho:
            Utils.titulo("Cadastro de Cliente")
        try:

            nome, email = Cliente.validar_nomes()
            id_cliente = dao.inserir(nome, email)
            Utils.limpar_tela()
            if cadastro_pedido == True:
                return id_cliente
            Utils.messagem_success("Inserido com sucesso")

            while True:
                print("Deseja cadastar novo cliente?")
                print("1 - Sim")
                print("2 - Não")
                print("0 - Retornar ao menu anterior")
                opcao_selecionado = Utils.obtem_opcao_menu(1, 2)
                if opcao_selecionado == 1:
                    Utils.limpar_tela()
                    nome = ""
                    email = ""
                    Cliente.cadastro(
                        nome, email, exibe_cabecalho=True,)
                if opcao_selecionado == 2 or opcao_selecionado == 0:
                    Utils.limpar_tela()
                    break

        except Exception as e:
            Utils.messagem_error(e=e)
            return Cliente.cadastro(nome, email, exibe_cabecalho=False)

    @staticmethod
    def listar():
        clientes = dao.listar()
        Utils.limpar_tela()
        Utils.titulo("Relatório de Clientes")
        for cliente in clientes:
            print(f"\ncodigo: {cliente.id}")
            print(f"Nome: {cliente.nome}")
            print(f"Email: {cliente.email}")
            print(f"{cor.CTEXTINFO}{'-' * 30}{cor.CEND}")
        input("Digite enter para sair do relatório \n")
        Utils.limpar_tela()

    def validar_nomes(nome='', email=''):
        try:
            if nome.strip() == "":
                nome = input("Digite o nome do cliente:")
                if nome.strip() == "":
                    raise TypeError("Digite o nome correto.")
            email = input("Digite o e-mail:")
            if email.strip() == "":
                raise TypeError("Email inválido.")
            if Utils.validar_email(email) == False:
                raise TypeError("Email inválido.")
            return nome, email
        except Exception as e:
            Utils.messagem_error(e=e)
            return Cliente.validar_nomes(nome, email)

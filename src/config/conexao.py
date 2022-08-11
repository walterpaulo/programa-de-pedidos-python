import os
import psycopg2
from mysql.connector import Error


class Conexao():

    @staticmethod
    def conectar():
        connection = None
        try:
            connection = psycopg2.connect(host=os.getenv("DATABASE_IP"), database='meuteste',
                                          user=os.getenv("DATABASE_USER"), password=os.getenv("DATABASE_PASSWORD"))
            # print("Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

        return connection

    @staticmethod
    def fechar_conexao(conn):
        try:
            if (conn != None):
                conn.close()
        except Error as err:
            print(f"Error: '{err}'")
    
    @staticmethod
    def main():
        try:
            Conexao.conectar()
            # print("Conexão efetuado com sucesso!")
        except Error as err:
            print(f"Error: '{err}'")

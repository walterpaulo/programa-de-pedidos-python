##### Não deixe o nome deste arquivo como init.py dá incompatibilidade ##########

"""
# para o S.O.
sudo apt update
sudo apt install mysql-server
sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root'; flush privileges;
mysql -uroot -p'root'
create database desafio_21_dias_python;
use desafio_21_dias_python;
CREATE TABLE usuarios (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    email VARCHAR(100) NOT NULL,
    endereco VARCHAR(255),
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
show tables;
select * from usuarios;
insert into usuarios(nome, email, endereco)
values('Danilo', 'danilo@torneseumprogramador.com.br', 'Rua teste');
select * from usuarios;
update usuarios set nome = 'Danilo', email = 'danilo@torneseumprogramador.com.br', endereco = 'Rua teste 123'
where id = 1;
select * from usuarios;
delete from usuarios where id=2;
select * from usuarios;
# instalando driver mysql pip
- https://pynative.com/python-mysql-database-connection/
# Pipenv - gerenciador de pacotes python
- https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv
# para o S.O.
sudo apt update
sudo apt-get install libmysqlclient-dev
sudo apt-get install libssl-dev
sudo apt-get install -y python3-mysqldb
sudo apt install python3-pip
git clone https://github.com/torneseumprogramador/desafio-logica-python
#### usando pip
pip install mysql-connector-python
python3 init.py 
#### usando pip env
sudo apt install pipenv # linux
brew install pipenv # macos
pipenv install
pipenv install mysql-connector-python
pipenv run python init.py 
pipenv shell # caso queira rodar sem "pipenv run"
python3 init.py 
"""

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

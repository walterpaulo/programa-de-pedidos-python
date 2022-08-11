# Loja de Pedidos

* linguagem -> Python 3.8;
* [Minhas Anotações e estudos](https://github.com/walterpaulo/logica-python) do "Desafio 21 dias de lógica em Python - Prof. Danilo Aparecido";

##  Exercício 

```s
Faça um programa para calcular os valores de um pedido
para isso crie uma classe de pedido que tenha relação com uma classe de cliente
nesse pedido, coloque uma propriedade de itens, contendo instancias de uma classe de produto
no pedido, crie um método para calcular o valor total 
e um método para mostrar um relatório do pedido, mostrando da seguinte forma:
----------------------------------------------------------------
Pedido Id: 1
Nome: João
Valor Total: R$ 999,99
----------------------------------------------------------------
O que terá na classe de pedido:
- id
- cliente
- metodo_valor_total()
- itens []
O que terá na classe cliente:
- Nome
- email
O que terá na classe produto:
- Nome
- descrição
- preço
```

## Estrutura do Código

```s
.
├── init.py
├── README.md
└── src/
    ├── config/
    │   └── conexao.py
    ├── controllers/
    │   ├── clientes_controller.py
    │   ├── home_controller.py
    │   ├── pedidos_controller.py
    │   ├── produtos_controller.py
    │   └── relatorios_controller.py
    ├── dao/
    │   ├── cliente_dao.py
    │   ├── dto/
    │   │   └── pedido_dto.py
    │   ├── pedido_dao.py
    │   └── produto_dao.py
    ├── models/
    │   ├── cliente_model.py
    │   ├── item_model.py
    │   ├── pedido_model.py
    │   └── produto_model.py
    ├── styles/
    │   └── cores.py
    ├── utils/
    │   └── utils.py
    └── views/
        ├── cliente.py
        ├── pedido.py
        └── produto.py
```

## Iniciar
```
python3 init.py
```

# Bancos
```sql
# POSTGRESQL
CREATE TABLE clientes
(
  id SERIAL,
  nome character(20),
  email character(30),
  CONSTRAINT pk_cliente PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);


CREATE TABLE produtos
(
  id SERIAL,
  nome character(20),
  preco money,
  CONSTRAINT pk_produto PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);

CREATE TABLE pedidos
(
  id SERIAL,
  id_cliente integer,
  itens character(200),
  CONSTRAINT pk_pedido PRIMARY KEY (id),
  CONSTRAINT "FK_pedidos_id_cliente" FOREIGN KEY (id_cliente)
      REFERENCES clientes (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
```
"""Faça um programa que crie o banco de dados preços.db com a
   tabela preços para armazenar uma lista de preços de venda de produtos. A tabela
   deve conter o nome do produto e seu respectivo preço. O programa também deve
   inserir alguns dados para teste."""

import sqlite3

conexao = sqlite3.connect('precos.db')
cursor = conexao.cursor()

cursor.execute('''
    create table if not exists precos(
        produto text,
        preço text)
        ''')

cursor.execute('''
    insert into precos (produto, preço)
    values(?,?)
    ''', ('Macarrão', 'R$9,99'))

conexao.commit()
cursor.close()
conexao.close()

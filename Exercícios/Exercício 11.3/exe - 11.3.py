""" Escreva um programa que realize consultas do banco de dados
    preços.db, criado no exercício 11.1. O programa deve perguntar o nome
    do produto e listar seu preço"""

import sqlite3

produto = input('De qual produto gostaria de listar o preço? ')

conexao = sqlite3.connect('precos.db')
cursor = conexao.cursor()
cursor.execute(f'select * from precos where nome = "{produto}"')

resultado = cursor.fetchone()
print(resultado)




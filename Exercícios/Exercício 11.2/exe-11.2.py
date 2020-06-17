"""
Faça um programa para listar todos os preços do banco preços.db
"""

import sqlite3

conexao = sqlite3.connect('precos.db')
cursor = conexao.cursor()

cursor.execute('select * from precos')

resultado = cursor.fetchone() # Retorna em forma de tupla

print(f'Produto: {resultado[0]}, Preço: {resultado[1]}')

conexao.commit()
cursor.close()
conexao.close()

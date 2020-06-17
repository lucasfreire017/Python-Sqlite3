import _sqlite3

conexao = _sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('select * from agenda')

# fetchall retorna uma lista com os resultados da consulta
resultado = cursor.fetchall()

for registro in resultado:
    print(f'Nome: {registro[0]}, Telefone {registro[1]}')
cursor.close()
conexao.close()
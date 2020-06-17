import sqlite3

nome = input('Nome a selecionar: ')

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute(f'select * from agenda where nome = "{nome}"')

while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print(f'Nome: {resultado[0]} \nTelefone: {resultado[1]}')

cursor.close()
conexao.close()

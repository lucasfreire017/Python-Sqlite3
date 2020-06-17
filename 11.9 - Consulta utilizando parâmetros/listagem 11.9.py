import sqlite3

nome = input('Nome a selecionar: ')
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('select * from agenda where nome = ?', (nome,))
x = 0

while True:
    resultado = cursor.fetchone()

    if resultado == None:
        if x == 0:
            print('nada encontrado.')
        break
    print(f'Nome: {resultado[0]} \nTelefone: {resultado[1]}')
    x+=1

cursor.close()
conexao.close()

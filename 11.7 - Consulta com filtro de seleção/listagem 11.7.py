import _sqlite3

conexao = _sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute("select * from agenda where nome = 'Nilo'")

while True:
    resultado = cursor.fetchone()
    if resultado == None:
        break

    print(f'Nome: {resultado[0]} \nTelefone: {resultado[1]}')

cursor.close()
conexao.close()

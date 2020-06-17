import _sqlite3

conexao = _sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('select * from agenda')

while True:
    # fechone retorna os valores um por um (útil para consultas longas)
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print(f'Nome: {resultado[0]}, Telefone: {resultado[1]}')
cursor.close()
conexao.close()

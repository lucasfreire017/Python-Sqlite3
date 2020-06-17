import _sqlite3
from contextlib import closing

with _sqlite3.connect('agenda.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('select * from agenda')
        while True:
            resultado = cursor.fetchone()
            if resultado == None:
                break
            print(f'Nome {resultado[0]}, Telefone {resultado[1]}')

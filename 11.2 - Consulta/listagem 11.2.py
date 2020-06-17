import _sqlite3

conexao = _sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute("select * from agenda")

# fetchone pega a consulta feira pelo cursor e retorna uma tupla
resultato = cursor.fetchone()
print(f'Nome: {resultato[0]} \nTelefone: {resultato[1]}')
cursor.close()
conexao.close()

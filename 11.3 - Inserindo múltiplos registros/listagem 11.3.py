import _sqlite3

dados = [ ('João', '98803-6797'),
          ('André', '96435-3124'),
          ('Maria', '97891-3321')]

conexao = _sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.executemany('''
    insert into agenda (nome, telefone)
    values(?,?)
    ''', dados)

conexao.commit()
cursor.close()
conexao.close()
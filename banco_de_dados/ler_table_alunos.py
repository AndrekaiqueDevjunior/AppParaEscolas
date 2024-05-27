import sqlite3

conn = sqlite3.connect('banco_de_dados.db')
cursor = conn.cursor()

SQL =  """PRAGMA table_info(alunos);"""
cursor.execute(SQL)
print(cursor.fetchall())
conn.close()





# SQL =  """ALTER TABLE alunos ADD COLUMN nome_da_mae TEXT;"""
# cursor.execute(SQL)
# conn.commit()
# conn.close()

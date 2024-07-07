import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('banco_de_dados/login.db')

# Criar um cursor
cursor = conn.cursor()

# Criar a tabela de usuários
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
)
''')

# Confirmar as mudanças e fechar a conexão
conn.commit()
conn.close()

print("Banco de dados e tabela 'usuarios' criados com sucesso!")

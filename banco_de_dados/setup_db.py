import sqlite3
import os

# Certifique-se de que o diretório para o banco de dados exista
os.makedirs('banco_de_dados', exist_ok=True)

# Conectar ao banco de dados (será criado se não existir)
conn = sqlite3.connect('banco_de_dados/banco_de_dados.db')
cursor = conn.cursor()

# Criar a tabela 'alunos' se ela não existir
SQL = """
CREATE TABLE IF NOT EXISTS alunos (
  id INTEGER PRIMARY KEY,
  nome TEXT NOT NULL
);
"""
cursor.execute(SQL)
conn.commit()
conn.close()

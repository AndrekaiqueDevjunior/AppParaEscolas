from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/salvar_aluno", methods=['POST'])
def salvar_aluno():
    data = request.get_json()
    print(data)
    
    conn = sqlite3.connect('banco_de_dados/banco_de_dados.db')
    cursor = conn.cursor()
    
    SQL = """INSERT INTO 
        alunos (
            nome,
            sobre_nome,
            nome_do_pai,
            nome_da_mae,
            data_de_nascimento,
            telefone,
            cpf,
            logradouro,
            rua,
            bairro,
            cidade,
            estado,
            cep      
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
    
    cursor.execute(SQL, 
    (
        data['nome'],
        data['sobre_nome'],
        data['nome_do_pai'],
        data['nome_da_mae'],
        data['data_de_nascimento'],
        data['telefone'],
        data['cpf'],
        data['logradouro'],
        data['rua'],
        data['bairro'],
        data['cidade'],
        data['estado'],
        data['cep']
    ))
    
    conn.commit()
    conn.close()
    
    return jsonify(retorno="Sucesso")

@app.route("/ler_todos_alunos", methods=['POST'])
def ler_todos_alunos():
    conn = sqlite3.connect('banco_de_dados/banco_de_dados.db')
    cursor = conn.cursor()
    
    SQL = """SELECT * FROM alunos;"""
    cursor.execute(SQL)
    dados = cursor.fetchall()
    print(dados)
    
    conn.close()
    return jsonify(dados=dados)

@app.route("/ler_aluno_especifico", methods=['POST'])
def ler_aluno_especifico():
    dict = request.get_json()
    conn = sqlite3.connect('banco_de_dados/banco_de_dados.db')
    cursor = conn.cursor()
    
    SQL = """ SELECT * FROM alunos WHERE id =""" + str(dict['id']) + """ ;""" 
    cursor.execute(SQL)
    dados = cursor.fetchall()
    
    SQL = """ PRAGMA table_info(alunos);""" 
    cursor.execute(SQL)
    cabecalho = cursor.fetchall()
    
    
    conn.close()
    return jsonify(
    dados=dados,
    cabecalho = cabecalho
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

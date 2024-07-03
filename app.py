from flask import Flask, render_template, request, jsonify, g, redirect, url_for, send_from_directory
import sqlite3
import os

app = Flask(__name__)
<<<<<<< HEAD
app.config['UPLOAD_PATH'] = 'uploads'  # Diretório onde os arquivos enviados serão salvos
=======
app.config['UPLOAD_PATH'] = 'uploads'
>>>>>>> c327f9952d6ec8ced141068397d3dfe80c482fd5


@app.route("/aluno")
def aluno():
    return render_template('alunos_login/aluno.html')  # Renderiza a página do Aluno

@app.route("/professor")
def professor():
    return render_template('professores_login/professor.html')  # Renderiza a página do Professor


#URL /
#ROTA / 
#DESCRICAO / = EXIBIR A PAGINA INICIAL DO SITE
# MÉTODO GET
@app.route("/")  ###INDEX
def index():
<<<<<<< HEAD
    return render_template('login/login.html')  # Renderiza a página login.html

@app.before_request
def before_request():
    g.conn = sqlite3.connect('banco_de_dados/banco_de_dados.db')  # Conecta ao banco de dados SQLite
    g.cursor = g.conn.cursor()  # Cria um cursor para executar comandos SQL
    print("Antes")  # Mensagem de depuração

@app.after_request
def after_request(response):
    print("Depois")  # Mensagem de depuração
    g.conn.commit()  # Confirma (commit) qualquer alteração no banco de dados
    g.conn.close()  # Fecha a conexão com o banco de dados
    return response  # Retorna a resposta

@app.route("/salvar_aluno", methods=['POST'])
def salvar_aluno():
    dict = request.get_json()  # Obtém dados JSON da requisição

    # Se o ID estiver vazio, insere um novo aluno
=======
    return render_template('index.html')

@app.before_request
def before_request():
    g.conn = sqlite3.connect('banco_de_dados/banco_de_dados.db')
    g.cursor = g.conn.cursor()

    print("Antes")

@app.after_request
def after_request(response):
    print("Depois")
    g.conn.commit()
    g.conn.close()
    return response

@app.route("/salvar_aluno", methods=['POST'])
def salvar_aluno():
    dict = request.get_json()
            
    # conn = sqlite3.connect('banco_de_dados/banco_de_dados.db')
    # cursor = conn.cursor()
    
    ## Quando é Alterar tem ID
    ## Quando é Inserir não ID
>>>>>>> c327f9952d6ec8ced141068397d3dfe80c482fd5
    if dict['id'] == '':        
        SQL = """ INSERT INTO
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
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);"""
        
        g.cursor.execute(SQL,
            (
                dict['nome'],
                dict['sobre_nome'],
                dict['nome_do_pai'],
                dict['nome_da_mae'],
                dict['data_de_nascimento'],
                dict['telefone'],
                dict['cpf'],
                dict['logradouro'],
                dict['rua'],
                dict['bairro'],
                dict['cidade'],
                dict['estado'],
                dict['cep'],
            )
        )
    else:  # Caso contrário, atualiza o aluno existente
        SQL = """ UPDATE alunos 
                SET
                    nome = ?,
                    sobre_nome = ?,
                    nome_do_pai = ?,
                    nome_da_mae = ?,
                    data_de_nascimento = ?,
                    telefone = ?,
                    cpf = ?,
                    logradouro = ?,
                    rua = ?,
                    bairro = ?,
                    cidade = ?,
                    estado = ?,
                    cep = ?         
                WHERE id = ?;"""
        g.cursor.execute(SQL,
            (
                dict['nome'],
                dict['sobre_nome'],
                dict['nome_do_pai'],
                dict['nome_da_mae'],
                dict['data_de_nascimento'],
                dict['telefone'],
                dict['cpf'],
                dict['logradouro'],
                dict['rua'],
                dict['bairro'],
                dict['cidade'],
                dict['estado'],
                dict['cep'],
                dict['id'],
            )
        )
        
<<<<<<< HEAD
    return jsonify(retorno="Sucesso")  # Retorna uma resposta JSON indicando sucesso
  
@app.route("/atualiza_foto", methods=['POST'])
def atualiza_foto():
    print(request.form['id_do_aluno'])  # Imprime o ID do aluno para depuração
    uploaded_file = request.files['file']  # Obtém o arquivo enviado
    if uploaded_file.filename != '':  # Se o nome do arquivo não estiver vazio
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], request.form['id_do_aluno'] + '.png'))  # Salva o arquivo no diretório de uploads
        
    return redirect('/')  # Redireciona para a página inicial

@app.route("/ler_todos_alunos", methods=['POST'])
def ler_todos_alunos():
    SQL = """ SELECT * FROM alunos;"""  # SQL para selecionar todos os alunos
    
    g.cursor.execute(SQL)  # Executa o comando SQL
    dados = g.cursor.fetchall()  # Obtém todos os resultados
    
    return jsonify(dados=dados)  # Retorna os dados em formato JSON

@app.route("/exclui_aluno", methods=['POST'])
def exclui_aluno():
    dict = request.get_json()  # Obtém dados JSON da requisição

    SQL = """ DELETE FROM alunos WHERE id=""" + str(dict['id']) + """;"""  # SQL para excluir um aluno

    g.cursor.execute(SQL)  # Executa o comando SQL
    
    return jsonify(x=0)  # Retorna uma resposta JSON

@app.route("/ler_aluno_especifico", methods=['POST'])
def ler_aluno_especifico():
    dict = request.get_json()  # Obtém dados JSON da requisição

    SQL = """ SELECT * FROM alunos WHERE id=""" + str(dict['id']) + """;"""  # SQL para selecionar um aluno específico
    g.cursor.execute(SQL)  # Executa o comando SQL
    dados = g.cursor.fetchall()  # Obtém os resultados
    
    SQL = """ PRAGMA table_info(alunos);"""  # SQL para obter informações sobre a estrutura da tabela
    g.cursor.execute(SQL)
    cabecalho = g.cursor.fetchall()  # Obtém as informações sobre a tabela
    
=======
    
    # conn.commit()
    # conn.close()
    return jsonify(retorno="Sucesso")
  
@app.route("/atualiza_foto", methods=['POST'])
def atualiza_foto():
    print(request.form['id_do_aluno'] )
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], request.form['id_do_aluno'] + '.png'))
        
    return redirect('/')

@app.route("/ler_todos_alunos", methods=['POST'])
def ler_todos_alunos():
    # conn = sqlite3.connect('banco_de_dados/banco_de_dados.db')
    # cursor = conn.cursor()
    SQL = """ SELECT * FROM alunos;"""
    
    g.cursor.execute(SQL)
    dados = g.cursor.fetchall()
    
    # conn.close()
    return jsonify(dados=dados)

@app.route("/exclui_aluno", methods=['POST'])
def exclui_aluno():
    dict = request.get_json()

    # conn = sqlite3.connect('banco_de_dados/banco_de_dados.db')
    # cursor = conn.cursor()
    SQL = """ DELETE FROM alunos WHERE id=""" + str(dict['id']) + """;"""

    g.cursor.execute(SQL)
    
    # conn.commit()
    # conn.close()
    return jsonify(x=0)

@app.route("/ler_aluno_especifico", methods=['POST'])
def ler_aluno_especifico():
    dict = request.get_json()

    # conn = sqlite3.connect('banco_de_dados/banco_de_dados.db')
    # cursor = conn.cursor()

    SQL = """ SELECT * FROM alunos WHERE id=""" + str(dict['id']) + """;"""
    g.cursor.execute(SQL)
    dados = g.cursor.fetchall()
    
    SQL = """ PRAGMA table_info(alunos);"""
    g.cursor.execute(SQL)
    cabecalho = g.cursor.fetchall()
    
        
    # conn.close()
>>>>>>> c327f9952d6ec8ced141068397d3dfe80c482fd5
    return jsonify(
        dados=dados,
        cabecalho=cabecalho
    )  # Retorna os dados e o cabeçalho em formato JSON

@app.route('/uploads/<filename>')
def upload(filename):
<<<<<<< HEAD
    return send_from_directory(app.config['UPLOAD_PATH'], filename)  # Envia o arquivo solicitado do diretório de uploads

app.run(debug=True, host='0.0.0.0')  # Inicia o servidor Flask em modo de depuração
=======
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

app.run(debug=True, host='0.0.0.0')
>>>>>>> c327f9952d6ec8ced141068397d3dfe80c482fd5

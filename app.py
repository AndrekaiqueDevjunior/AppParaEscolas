from flask import Flask, render_template, request, redirect, url_for, flash, g, session
import sqlite3
import os
from werkzeug.utils import secure_filename
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'templates/uploads'  # Diretório onde os arquivos enviados serão salvos
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.secret_key = 'your_secret_key'  # Chave secreta para a aplicação Flask

bcrypt = Bcrypt(app)

# Função para obter conexão com o banco de dados SQLite
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('banco_de_dados/banco_de_dados.db')
    return g.db

# Fechar a conexão com o banco de dados após cada requisição
@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Função para verificar se o email já existe no banco de dados
def email_exists(email):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT 1 FROM usuarios WHERE email = ?", (email,))
    result = cursor.fetchone()
    db.close()
    return result is not None

# Rota para cadastrar um novo professor
@app.route("/professor/new", methods=['GET', 'POST'])
def cadastro_professor():
    if request.method == 'POST':
        # Obter dados do formulário
        nome_completo = request.form['nome_completo']
        senha = bcrypt.generate_password_hash(request.form['senha']).decode('utf-8')
        email = request.form['email']
        telefone = request.form['telefone']
        formacao_academica = request.form['formacao_academica']
        areas_especializacao = request.form['areas_especializacao']
        numero_registro_profissional = request.form['numero_registro_profissional']
        
        # Obter arquivos enviados
        experiencia_profissional = request.files['experiencia_profissional']
        foto_de_perfil = request.files['foto_de_perfil']
        
        # Verificar se o email já está registrado
        if email_exists(email):
            flash('Email já registrado')
            return redirect(url_for('cadastro_professor'))
        
        # Salvar os arquivos enviados
        experiencia_profissional_filename = secure_filename(experiencia_profissional.filename)
        foto_de_perfil_filename = secure_filename(foto_de_perfil.filename)
        experiencia_profissional.save(os.path.join(app.config['UPLOAD_PATH'], experiencia_profissional_filename))
        foto_de_perfil.save(os.path.join(app.config['UPLOAD_PATH'], foto_de_perfil_filename))
        
        # Conectar ao banco de dados e inserir os dados do professor
        db = get_db()
        try:
            db.execute('''
                INSERT INTO professores (nome_completo, senha, email, telefone, formacao_academica, areas_especializacao, numero_registro_profissional, experiencia_profissional, foto_de_perfil) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nome_completo, senha, email, telefone, formacao_academica, areas_especializacao, numero_registro_profissional, experiencia_profissional_filename, foto_de_perfil_filename))
            db.commit()
            return redirect(url_for('professor'))  # Redirecionar após o cadastro bem-sucedido
        except sqlite3.IntegrityError:
            flash('Erro ao cadastrar professor')
        finally:
            db.close()

    return render_template('professores_login/cadastro_professor.html')  # Renderizar página de cadastro de professor

# Rota para cadastrar um novo aluno
@app.route("/aluno/new", methods=['GET', 'POST'])
def cadastro_aluno():
    if request.method == 'POST':
        # Obter dados do formulário
        nome = request.form['nome_completo']
        email = request.form['email']
        senha = bcrypt.generate_password_hash(request.form['senha']).decode('utf-8')
        telefone = request.form['telefone']
        formacao_academica = request.form['formacao_academica']
        areas_especializacao = request.form['areas_especializacao']
        numero_registro_profissional = request.form['numero_registro_profissional']
        
        # Obter arquivos enviados
        experiencia_profissional = request.files['experiencia_profissional']
        foto_de_perfil = request.files['foto_de_perfil']
        
        # Verificar se o email já está registrado
        if email_exists(email):
            flash('Email já registrado')
            return redirect(url_for('cadastro_aluno'))
        
        # Salvar os arquivos enviados
        experiencia_profissional_filename = secure_filename(experiencia_profissional.filename)
        foto_de_perfil_filename = secure_filename(foto_de_perfil.filename)
        experiencia_profissional.save(os.path.join(app.config['UPLOAD_PATH'], experiencia_profissional_filename))
        foto_de_perfil.save(os.path.join(app.config['UPLOAD_PATH'], foto_de_perfil_filename))
        
        # Conectar ao banco de dados e inserir os dados do aluno
        db = get_db()
        try:
            db.execute('''
                INSERT INTO alunos (nome_completo, email, senha, telefone, formacao_academica, areas_especializacao, numero_registro_profissional, experiencia_profissional, foto_de_perfil) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (nome, email, senha, telefone, formacao_academica, areas_especializacao, numero_registro_profissional, experiencia_profissional_filename, foto_de_perfil_filename))
            db.commit()
            return redirect(url_for('aluno'))  # Redirecionar após o cadastro bem-sucedido
        except sqlite3.IntegrityError:
            flash('Erro ao cadastrar aluno')
        finally:
            db.close()
    
    return render_template('alunos_login/cadastro_aluno.html')  # Renderizar página de cadastro de aluno

# Rota para página de login do aluno
@app.route("/aluno") 
def aluno():
    return render_template('alunos_login/aluno.html')  # Renderizar página de login do aluno

# Rota para página de login do professor
@app.route("/professor")
def professor():
    return render_template('/professores_login/professor.html')  # Renderizar página de login do professor

# Rota para o menu do professor
@app.route("/menu_professor")
def menu_professor():
    return render_template('professores_login/menu_professor.html')  # Renderizar menu do professor

# Rota para o menu do aluno
@app.route('/menu_aluno')
def menu_aluno():
    return render_template('menu_aluno.html')  # Renderizar menu do aluno

# Rota para página inicial do site
@app.route("/")  
def index():
    return render_template('login/login.html')  # Renderizar página de login inicial

# Função executada antes de cada requisição
@app.before_request
def before_request():
    g.conn = sqlite3.connect('banco_de_dados/banco_de_dados.db')  # Conectar ao banco de dados SQLite
    g.cursor = g.conn.cursor()  # Criar cursor para executar comandos SQL

# Função executada após cada requisição
@app.after_request
def after_request(response):
    g.conn.commit()  # Confirmar (commit) qualquer alteração no banco de dados
    g.conn.close()  # Fechar a conexão com o banco de dados
    return response  # Retornar a resposta

# Rota para o login de usuário
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        tipo_usuario = request.form['tipo_usuario']

        db = get_db()
        cursor = db.cursor()

        if tipo_usuario == 'aluno':
            cursor.execute("SELECT * FROM alunos WHERE email = ?", (email,))
            user = cursor.fetchone()
            db.close()
            if user and bcrypt.check_password_hash(user[2], senha):  # Alterar índice do campo senha conforme a estrutura da tabela alunos
                session['user_id'] = user[0]
                session['username'] = user[1]
                return redirect(url_for('aluno'))  # Redirecionar para página do aluno após login
            else:
                flash('Credenciais inválidas')
                return redirect(url_for('index'))

        elif tipo_usuario == 'professor':
            cursor.execute("SELECT * FROM professores WHERE email = ?", (email,))
            user = cursor.fetchone()
            db.close()
            if user and bcrypt.check_password_hash(user[1], senha):  # Alterar índice do campo senha conforme a estrutura da tabela professores
                session['user_id'] = user[0]
                session['username'] = user[1]
                return redirect(url_for('menu_professor'))  # Redirecionar para página do professor após login
            else:
                flash('Credenciais inválidas')
                return redirect(url_for('index'))

    return render_template('login/login.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Iniciar servidor Flask em modo de depuração

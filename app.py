from flask import Flask, render_template, request, jsonify, g, redirect, url_for, send_from_directory, session, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessário para usar sessões e mensagens flash
app.config['UPLOAD_PATH'] = 'uploads'
DATABASE = 'banco_de_dados/banco_de_dados.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

@app.before_request
def before_request():
    g.db = get_db()
    g.cursor = g.db.cursor()

@app.after_request
def after_request(response):
    db = getattr(g, 'db', None)
    if db is not None:
        db.commit()
        db.close()
    return response

@app.route("/")
def login_usuario():
    return render_template('login_usuario/logar_usuario.html')

@app.route("/index")
def index():
    if 'user_id' not in session:
        return redirect(url_for('login_usuario'))
    return render_template('index.html')

@app.route("/cadastro")
def criar_aluno():
    return render_template('criar_aluno/criar_usuario.html')

@app.route("/autenticar_usuario", methods=['POST'])
def autenticar_usuario():
    email = request.form['email']
    senha = request.form['senha']
    
    SQL = """ SELECT id FROM usuarios WHERE email=? AND senha=? """
    g.cursor.execute(SQL, (email, senha))
    user = g.cursor.fetchone()
    
    if user:
        session['user_id'] = user[0]
        return redirect(url_for('index'))
    else:
        flash('Email ou senha incorretos.')
        return redirect(url_for('login_usuario'))

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login_usuario'))

@app.route("/salvar_aluno", methods=['POST'])
def salvar_aluno():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    senha = request.form['senha']
    
    try:
        SQL = """ INSERT INTO usuarios (nome, sobrenome, email, senha) VALUES (?, ?, ?, ?); """
        g.cursor.execute(SQL, (nome, sobrenome, email, senha))
        flash('Usuário cadastrado com sucesso!')
    except sqlite3.IntegrityError:
        flash('O email fornecido já está em uso.')
    
    return redirect(url_for('login_usuario'))

@app.route("/atualiza_foto", methods=['POST'])
def atualiza_foto():
    print(request.form['id_do_aluno'])
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], request.form['id_do_aluno'] + '.png'))
        
    return redirect('/')

@app.route("/ler_todos_alunos", methods=['POST'])
def ler_todos_alunos():
    SQL = """ SELECT * FROM alunos;"""
    g.cursor.execute(SQL)
    dados = g.cursor.fetchall()
    return jsonify(dados=dados)

@app.route("/exclui_aluno", methods=['POST'])
def exclui_aluno():
    data = request.get_json()
    SQL = """ DELETE FROM alunos WHERE id=?;"""
    g.cursor.execute(SQL, (data['id'],))
    return jsonify(x=0)

@app.route("/ler_aluno_especifico", methods=['POST'])
def ler_aluno_especifico():
    data = request.get_json()
    SQL = """ SELECT * FROM alunos WHERE id=?;"""
    g.cursor.execute(SQL, (data['id'],))
    dados = g.cursor.fetchall()
    
    SQL = """ PRAGMA table_info(alunos);"""
    g.cursor.execute(SQL)
    cabecalho = g.cursor.fetchall()
        
    return jsonify(
        dados=dados,
        cabecalho=cabecalho
    )

@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

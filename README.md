### MANUAL PARA EXECUTAR O SOFTWARE GRATUITO PARA ESCOLAS (MULTIFUNCIONALIDADE WEB)
Este manual fornece instruções detalhadas para configurar e executar o software multifuncional para escolas em dispositivos móveis e computadores. Siga os passos abaixo para montar seu ambiente de desenvolvimento.

### Itens Necessários
1. **Python 3.9**
2. **Flask** (qualquer versão de 2024)
3. **Noções básicas em prompt de comando** (tanto faz se for Windows ou Linux)

### Passo a Passo

#### 1. Instalação do Python 3.9

##### Windows:
1. Baixe o instalador do Python 3.9 do site oficial: [Python.org](https://www.python.org/downloads/release/python-390/)
2. Execute o instalador e siga as instruções na tela. Certifique-se de marcar a opção "Add Python to PATH".
3. Verifique a instalação abrindo o Prompt de Comando (CMD) e digitando:
   ```sh
   python --version
   ```

##### Linux:
1. Atualize o gerenciador de pacotes:
   ```sh
   sudo apt update
   ```
2. Instale o Python 3.9:
   ```sh
   sudo apt install python3.9
   ```
3. Verifique a instalação:
   ```sh
   python3.9 --version
   ```

#### 2. Configuração do Ambiente Virtual

1. Crie um ambiente virtual para o projeto:
   ```sh
   python -m venv venv
   ```
2. Ative o ambiente virtual:
   - **Windows:**
     ```sh
     venv\Scripts\activate
     ```
   - **Linux:**
     ```sh
     source venv/bin/activate
     ```

#### 3. Instalação do Flask

1. Certifique-se de que o ambiente virtual está ativo.
2. Instale o Flask:
   ```sh
   pip install Flask
   ```

#### 4. Configuração do Projeto Flask

1. Crie um diretório para o projeto:
   ```sh
   mkdir meu_projeto
   cd meu_projeto
   ```
2. Crie um arquivo `app.py` com o seguinte conteúdo:
   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def home():
       return "Bem-vindo ao Software para Escolas!"

   if __name__ == '__main__':
       app.run(debug=True)
   ```

#### 5. Executando o Projeto

1. No terminal, estando no diretório do projeto e com o ambiente virtual ativo, execute:
   ```sh
   python app.py
   ```
2. Abra um navegador web e acesse `http://127.0.0.1:5000` para ver a aplicação em execução.

#### 6. Acessando no Mobile
Certifique-se de que seu dispositivo móvel e seu computador estão na mesma rede Wi-Fi. No computador, encontre o endereço IP local:
```sh
ipconfig (Windows)
ifconfig (Linux)
```
Substitua `127.0.0.1` pelo IP local no navegador do seu dispositivo móvel.

### Comandos Resumidos

#### Para Windows:
```sh
# Instalação do Python
python --version

# Ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instalação do Flask
pip install Flask

# Criar e executar o app Flask
mkdir meu_projeto
cd meu_projeto
echo from flask import Flask > app.py
echo app = Flask(__name__) >> app.py
echo @app.route('/') >> app.py
echo def home(): >> app.py
echo return "Bem-vindo ao Software para Escolas!" >> app.py
echo if __name__ == '__main__': >> app.py
echo app.run(debug=True) >> app.py
python app.py
```

#### Para Linux:
```sh
# Instalação do Python
sudo apt update
sudo apt install python3.9
python3.9 --version

# Ambiente virtual
python3.9 -m venv venv
source venv/bin/activate

# Instalação do Flask
pip install Flask

# Criar e executar o app Flask
mkdir meu_projeto
cd meu_projeto
echo "from flask import Flask" > app.py
echo "app = Flask(__name__)" >> app.py
echo "@app.route('/')" >> app.py
echo "def home():" >> app.py
echo "    return 'Bem-vindo ao Software para Escolas!'" >> app.py
echo "if __name__ == '__main__':" >> app.py
echo "    app.run(debug=True)" >> app.py
python app.py
```

Com esses passos, você deve ser capaz de configurar e executar o software para escolas em seu ambiente de desenvolvimento.

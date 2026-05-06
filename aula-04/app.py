# Cometário dem Python
# Importando o Flask na aplicação
from flask import Flask, render_template 
from controllers import routes
#Render template renderiz as paginas HTML

import pymysql
from models.database import db, Game


# Carregando o Flask em uma variável 
# Declarando variável no Python
app = Flask(__name__, template_folder='views')
# __name__ é uma variável de ambiente de phyton que tem o nome do módulo atual

# Enviar app para as rotas

DB_NAME = 'thegames'

app.config['DATABASE_NAME'] = DB_NAME

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'

routes.init_app(app)

# Iniciando o servidor web
if __name__ == '__main__':
    
    # Dados e Conexão com o banco
    connection = pymysql.connect(host='localhost', user='root', password='', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    
    try:
        with connection.cursor() as cursor:
            
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print("O banco de dados foi criado com êxito")
    except Exception as error:
        print(f"Erro ao criar o banco de dados: {error}")
    finally:
        connection.close()   
        
        
    #Iniciar o sqlAlchemy
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    
    app.run(debug=True) #Ligando modo de depuração, reinicia automático
# .run inicia um servidor
# verificando se o app.py for o arquivo principal, ele inicia o servidor

# Ctrl + " = abre o terminal
# python app.py + enter = running...ip(local)
# Ctrl + clicar no ip -> not found ( navegador)
# porta padrão no python -> :5000
# Ctrl + C -> parar o servidor

# Cometário dem Python
# Importando o Flask na aplicação
from flask import Flask, render_template 
from controllers import routes
#Render template renderiz as paginas HTML

# Carregando o Flask em uma variável 
# Declarando variável no Python
app = Flask(__name__, template_folder='views')
# __name__ é uma variável de ambiente de phyton que tem o nome do módulo atual

# Enviar app para as rotas

routes.init_app(app)

# Iniciando o servidor web
if __name__ == '__main__':
    app.run(debug=True) #Ligando modo de depuração, reinicia automático
# .run inicia um servidor
# verificando se o app.py for o arquivo principal, ele inicia o servidor

# Ctrl + " = abre o terminal
# python app.py + enter = running...ip(local)
# Ctrl + clicar no ip -> not found ( navegador)
# porta padrão no python -> :5000
# Ctrl + C -> parar o servidor

from flask import Flask, render_template 
from controllers import routes

app = Flask(__name__, template_folder='views')
routes.init_app(app)

if __name__ == '__main__':
    app.run(debug=True) #Ligando modo de depuração, reinicia automático
# .run inicia um servidor
# verificando se o app.py for o arquivo principal, ele inicia o servidor


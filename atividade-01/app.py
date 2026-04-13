from flask import Flask, render_template 

app = Flask(__name__, template_folder='views')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bestiary')
def bestiary():
    return render_template('bestiary.html')

@app.route('/locations')
def locations():
    return render_template('locations.html')

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True) #Ligando modo de depuração, reinicia automático
# .run inicia um servidor
# verificando se o app.py for o arquivo principal, ele inicia o servidor


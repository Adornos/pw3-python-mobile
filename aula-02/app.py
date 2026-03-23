# Cometário dem Python
# Importando o Flask na aplicação
from flask import Flask, render_template 
#Render template renderiz as paginas HTML

# Carregando o Flask em uma variável 
# Declarando variável no Python
app = Flask(__name__, template_folder='views')
# __name__ é uma variável de ambiente de phyton que tem o nome do módulo atual

# Criando a rota principal do site 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/games')
def games():
    #Variaveis da pagina de gaems
    game = {
    "titulo": 'SilkSong',
    "descricao":'SilkSong é um jogo de ação e aventura desenvolvido pela Team Cherry, conhecido por seu estilo artístico encantador e jogabilidade desafiadora. O jogo se passa em um mundo subterrâneo repleto de criaturas misteriosas e ambientes deslumbrantes. Os jogadores assumem o papel de uma pequena criatura chamada Hornet, que embarca em uma jornada para descobrir os segredos do reino de Hallownest. Com uma combinação de exploração, combate e habilidades únicas, SilkSong promete oferecer uma experiência envolvente para os fãs de jogos indie e amantes de aventuras emocionantes.',
    "ano": 2025,
    "categoria":'Metroidvania'
    }
    
    jogadores = ['Guilherme', 'Maria', 'João', 'Ana']

    return render_template('games.html', game=game, jogadores=jogadores)

@app.route('/consoles')
def consoles(): 
    consolesDestaque= ['Nintendo Switch 2']
    consoles= ['Playstation 1', 'Playstation 2', 'Playstation 4', 'Playstation 5', 'Playstation 5']
    return render_template('consoles.html', consoles=consoles, consolesDestaque=consolesDestaque)
# def serve para criar funções no pythone home é o nome da função



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

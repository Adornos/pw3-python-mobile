from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

def init_app(app):

    listaGames = [{"titulo": "CS-GO", "ano": 2012, "categoria": "FPS"}]

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
    
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == "POST": #verificando se o metodo usado é o método POST
            # Recebendo os dados do formulário
            listaGames.append({"titulo": request.form.get('titulo'), "ano": request.form.get('ano'), "categoria": request.form.get('categoria')})
            return redirect(url_for('cadgames'))
            
        return render_template('cadgames.html', listaGames=listaGames)


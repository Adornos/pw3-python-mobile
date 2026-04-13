from flask import render_template

def init_app(app):


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


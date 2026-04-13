from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

def init_app(app):

    locations_data = [
        {
            "nome": "Aldoria",
            "regiao": "Reino de Valdren",
            "descricao": "Uma cidade próspera cercada por muralhas antigas, famosa por seus mercados e pela guilda dos mercadores."
        },
        {
            "nome": "Drakmor",
            "regiao": "Montanhas de Ferro Negro",
            "descricao": "Uma fortaleza cravada nas montanhas, lar de ferreiros lendários e rumores de dragões adormecidos."
        },
        {
            "nome": "Lunaris",
            "regiao": "Costa da Lua Prateada",
            "descricao": "Cidade portuária iluminada por um brilho constante da lua, conhecida por seus navegadores e mistérios marítimos."
        },
        {
            "nome": "Eryndor",
            "regiao": "Floresta de Sylvandor",
            "descricao": "Uma vila élfica escondida entre árvores gigantes, onde magia e natureza coexistem em perfeita harmonia."
        },
        {
            "nome": "Valkhar",
            "regiao": "Deserto Escarlate",
            "descricao": "Uma cidade construída ao redor de um oásis raro, habitada por comerciantes e caçadores de relíquias antigas."
        },
        {
            "nome": "Noctharyn",
            "regiao": "Terras Sombrias",
            "descricao": "Cidade envolta em névoa eterna, onde dizem que criaturas das sombras caminham livremente à noite."
        },
        {
            "nome": "Thalgrim",
            "regiao": "Planícies de Karvok",
            "descricao": "Centro militar estratégico, conhecido por seus cavaleiros e campos de treinamento rigorosos."
        },
        {
            "nome": "Mystral",
            "regiao": "Ilhas do Vento Azul",
            "descricao": "Cidade flutuante sustentada por magia antiga, lar de magos e estudiosos do arcano."
        }
    ]
    creatures_data = [
    {
        "nome": "Draconis Sombrio",
        "tipo": "Dragão",
        "nivel": 50,
        "descricao": "Uma criatura colossal que habita cavernas profundas, capaz de cuspir chamas negras e envolver seus inimigos em sombras."
    },
    {
        "nome": "Lobo de Gelo",
        "tipo": "Fera",
        "nivel": 12,
        "descricao": "Um predador das regiões congeladas, com olhos azuis brilhantes e uma pelagem resistente ao frio extremo."
    },
    {
        "nome": "Espectro Errante",
        "tipo": "Espírito",
        "nivel": 20,
        "descricao": "Uma alma perdida que vaga entre os vivos, drenando energia vital daqueles que cruzam seu caminho."
    },
    {
        "nome": "Golem de Pedra",
        "tipo": "Construto",
        "nivel": 30,
        "descricao": "Uma entidade criada por magia antiga, extremamente resistente e quase impossível de deter com armas comuns."
    },
    {
        "nome": "Serpente do Deserto",
        "tipo": "Monstro",
        "nivel": 18,
        "descricao": "Uma criatura gigantesca que se esconde sob a areia, atacando viajantes desavisados com rapidez mortal."
    },
    {
        "nome": "Aranha Sombria",
        "tipo": "Inseto",
        "nivel": 10,
        "descricao": "Habita florestas densas e ruínas abandonadas, tecendo teias venenosas e caçando silenciosamente."
    },
    {
        "nome": "Fênix Rubra",
        "tipo": "Mítico",
        "nivel": 45,
        "descricao": "Uma ave lendária que renasce das próprias cinzas, associada ao fogo e à imortalidade."
    },
    {
        "nome": "Cavaleiro Esqueleto",
        "tipo": "Morto-vivo",
        "nivel": 22,
        "descricao": "Um antigo guerreiro reanimado por magia sombria, condenado a lutar eternamente."
    }
]
    
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/bestiary')
    def bestiary():
        return render_template('bestiary.html', creatures=creatures_data)

    @app.route('/locations')
    def locations():
        return render_template('locations.html', locations=locations_data)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == "POST":
            nova_criatura = {
                "nome": request.form.get("name"),
                "tipo": request.form.get("type"),
                "nivel": int(request.form.get("level")),
                "descricao": request.form.get("description")
            }

            creatures_data.append(nova_criatura)

            return redirect(url_for('register'))

        return render_template('register.html', creatures=creatures_data)
    
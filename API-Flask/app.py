from flask import Flask
from controllers.alunos_controller import aluno_bp
from controllers.professores_controller import professor_bp
from controllers.turmas_controller import turma_bp
from config import db
from flasgger import Swagger

app = Flask(__name__)

# Configurações da aplicação
app.config['PORT'] = 5000
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SWAGGER'] = {
    "title": "DevAPI - Documentação com Swagger",
    "uiversion": 3
}

# Inicialização do banco e documentação
db.init_app(app)
swagger = Swagger(app)

# Registro dos blueprints
app.register_blueprint(aluno_bp, url_prefix="/alunos")
app.register_blueprint(professor_bp, url_prefix="/professores")
app.register_blueprint(turma_bp, url_prefix="/turmas")

# Rota principal estilizada
@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>DevAPI</title>
            <style>
                body {
                    margin: 0;
                    padding: 0;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    text-align: center;
                    color: #333;
                }
                h1 {
                    font-size: 2.5em;
                    color: #1e88e5;
                    margin: 0.2em 0;
                }
                p {
                    font-size: 1.1em;
                    margin: 0.3em 0;
                }
                .info {
                    color: #666;
                    font-weight: bold;
                }
                a {
                    background-color: #1e88e5;
                    color: white;
                    padding: 10px 20px;
                    border-radius: 6px;
                    text-decoration: none;
                    font-size: 1em;
                    box-shadow: 0 3px 6px rgba(0,0,0,0.1);
                    transition: background-color 0.3s ease, transform 0.2s ease;
                    margin-top: 0.5em;
                }
                a:hover {
                    background-color: #1565c0;
                    transform: scale(1.03);
                }
                .emoji {
                    font-size: 1.8em;
                    margin-bottom: 0.2em;
                }
            </style>
        </head>
        <body>
            <div class="emoji">🚀</div>
            <h1>Bem-vindo à <strong>DevAPI</strong></h1>
            <p>Explore nossa documentação e conheça os endpoints disponíveis.</p>
            <a href="/apidocs/">👉 Acessar Swagger Docs</a>
        </body>
        </html>
    '''

# Rota de teste
@app.route('/teste', methods=['GET'])
def teste():
    return {"message": "Tudo está funcionando corretamente!"}

# Criação das tabelas antes do primeiro uso
with app.app_context():
    db.create_all()

# Inicialização da aplicação
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
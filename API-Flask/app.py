import sys
from os.path import dirname, abspath
sys.path.append(dirname(abspath(__file__)))
from flask import Flask
from controllers.alunos_controller import aluno_bp
from controllers.professores_controller import professor_bp
from controllers.turmas_controller import turma_bp
from controllers.integracao_reservas_controller import integracao_reserva_bp
from controllers.integracao_atividades_controller import integracao_atividade_bp
from config import db
from flasgger import Swagger

sys.path.append(dirname(abspath(__file__)))

app = Flask(__name__)

@app.after_request
def add_cache_control(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

app.config['PORT'] = 5000
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SWAGGER'] = {
    'title': 'DevAPI',
    'uiversion': 3,
    'openapi': '3.0.0',
    'specs_route': '/apidocs/',
    'components': {
        'schemas': {
            'Aluno': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer', 'example': 1},
                    'nome': {'type': 'string', 'example': 'Henry Modesto'},
                    'idade': {'type': 'integer', 'example': 19},
                    'turma_id': {'type': 'integer', 'example': 1},
                    'data_nascimento': {'type': 'string', 'format': 'date', 'example': '2005-06-29'},
                    'nota_primeiro_semestre': {'type': 'number', 'format': 'float', 'example': 7.5},
                    'nota_segundo_semestre': {'type': 'number', 'format': 'float', 'example': 8.0},
                    'media_final': {'type': 'number', 'format': 'float', 'example': 7.75}
                }
            },
            'AlunoInput': {
                'type': 'object',
                'required': ['nome', 'idade', 'turma_id', 'data_nascimento', 
                            'nota_primeiro_semestre', 'nota_segundo_semestre'],
                'properties': {
                    'nome': {'type': 'string', 'example': 'Henry Modesto'},
                    'idade': {'type': 'integer', 'example': 19},
                    'turma_id': {'type': 'integer', 'example': 1},
                    'data_nascimento': {'type': 'string', 'format': 'date', 'example': '2005-06-29'},
                    'nota_primeiro_semestre': {'type': 'number', 'format': 'float', 'example': 7.5},
                    'nota_segundo_semestre': {'type': 'number', 'format': 'float', 'example': 8.0}
                }
            },
            'Professor': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer', 'example': 1},
                    'nome': {'type': 'string', 'example': 'Caio Ireno'},
                    'idade': {'type': 'integer', 'example': 25},
                    'materia': {'type': 'string', 'example': 'Desenvolvimento de APIs e Microsserviços'},
                    'observacoes': {'type': 'string', 'example': 'Professor titular'}
                }
            },
            'ProfessorInput': {
                'type': 'object',
                'required': ['nome', 'idade', 'materia'],
                'properties': {
                    'nome': {'type': 'string', 'example': 'Caio Ireno'},
                    'idade': {'type': 'integer', 'example': 25},
                    'materia': {'type': 'string', 'example': 'Desenvolvimento de APIs e Microsserviços'},
                    'observacoes': {'type': 'string', 'example': 'Professor titular'}
                }
            },
            
            'Turma': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer', 'example': 1},
                    'descricao': {'type': 'string', 'example': '3º Ano C'},
                    'professor_id': {'type': 'integer', 'example': 1},
                    'ativo': {'type': 'boolean', 'example': True}
                }
            },
            'TurmaInput': {
                'type': 'object',
                'required': ['descricao', 'professor_id'],
                'properties': {
                    'descricao': {'type': 'string', 'example': '3º Ano C'},
                    'professor_id': {'type': 'integer', 'example': 1},
                    'ativo': {'type': 'boolean', 'example': True}
                }
            }
        }
    }
}

db.init_app(app)
swagger = Swagger(app)

app.register_blueprint(aluno_bp, url_prefix="/alunos")
app.register_blueprint(professor_bp, url_prefix="/professores")
app.register_blueprint(turma_bp, url_prefix="/turmas")
app.register_blueprint(integracao_reserva_bp, url_prefix="/integracao")
app.register_blueprint(integracao_atividade_bp, url_prefix="/integracao")

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

@app.route('/teste')
def teste():
    return {"message": "Tudo está funcionando corretamente!"}

with app.app_context():
    from models.professores.professores import Professor
    from models.turmas.turmas import Turma
    from models.alunos.alunos import Aluno
    
    db.create_all()
    
    @db.event.listens_for(Aluno.nota_primeiro_semestre, 'set')
    @db.event.listens_for(Aluno.nota_segundo_semestre, 'set')
    def calcular_media(aluno, value, oldvalue, initiator):
        aluno.calcular_media()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
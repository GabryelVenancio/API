from config import app
from controllers.alunos_controller import alunos_bp
from controllers.professores_controller import professores_bp
from controllers.turmas_controller import turmas_bp

from flasgger import Swagger
swagger = Swagger(app)

app.register_blueprint(alunos_bp, url_prefix='/alunos')
app.register_blueprint(professores_bp, url_prefix='/professores')
app.register_blueprint(turmas_bp, url_prefix='/turmas')

@app.route('/')
def home():
    return {
        "mensagem": "Bem-vindo à API!",
        "rotas_disponiveis": ["/alunos", "/professores", "/turmas", "/apidocs/"]
    }

if __name__ == '__main__':
    app.run(
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )

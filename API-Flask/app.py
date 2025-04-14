from flask import Flask
from controllers.alunos_controller import alunos_bp
from controllers.professores_controller import professores_bp
from controllers.turmas_controller import turmas_bp

app = Flask(__name__)

app.config.from_pyfile('config.py')

app.register_blueprint(alunos_bp, url_prefix='/alunos')
app.register_blueprint(professores_bp, url_prefix='/professores')
app.register_blueprint(turmas_bp, url_prefix='/turmas')

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
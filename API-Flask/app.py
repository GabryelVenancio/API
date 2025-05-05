
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

professores = []
turmas = []
alunos = []

def validar_data(data_str):
    try:
        datetime.strptime(data_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Bem-vindo à API!"}), 200

@app.route('/professores', methods=['GET'])
def get_professores():
    return jsonify(professores)

@app.route('/professores', methods=['POST'])
def add_professor():
    data = request.get_json()
    if 'nome' not in data:
        return jsonify({"erro": "professor sem nome"}), 400
    if 'idade' not in data or data['idade'] <= 0:
        return jsonify({"erro": "idade invalida"}), 400
    if any(p['id'] == data['id'] for p in professores):
        return jsonify({"erro": "id ja utilizada"}), 400
    professores.append(data)
    return jsonify(data), 201

@app.route('/professores/<int:id>', methods=['GET'])
def get_professor(id):
    professor = next((p for p in professores if p['id'] == id), None)
    if professor:
        return jsonify(professor)
    return jsonify({"erro": "professor nao encontrado"}), 404

@app.route('/professores/<int:id>', methods=['PUT'])
def update_professor(id):
    data = request.get_json()
    professor = next((p for p in professores if p['id'] == id), None)
    if professor is None:
        return jsonify({"erro": "professor nao encontrado"}), 404
    if 'nome' not in data:
        return jsonify({"erro": "professor sem nome"}), 400
    professor.update(data)
    return jsonify(professor)

@app.route('/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    global professores
    if not any(p['id'] == id for p in professores):
        return jsonify({"erro": "professor nao encontrado"}), 404
    professores = [p for p in professores if p['id'] != id]
    return jsonify({"message": "Professor deletado com sucesso"})

@app.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify(turmas)

@app.route('/turmas', methods=['POST'])
def add_turma():
    data = request.get_json()
    if 'descricao' not in data:
        return jsonify({"erro": "turma sem descricao"}), 400
    if 'professor_id' not in data or not any(p['id'] == data['professor_id'] for p in professores):
        return jsonify({"erro": "professor nao encontrado"}), 400
    if 'ativo' not in data or not isinstance(data['ativo'], bool):
        return jsonify({"erro": "campo 'ativo' ausente ou invalido"}), 400
    if any(t['id'] == data['id'] for t in turmas):
        return jsonify({"erro": "id ja utilizada"}), 400
    turmas.append(data)
    return jsonify(data), 201

@app.route('/turmas/<int:id>', methods=['GET'])
def get_turma(id):
    turma = next((t for t in turmas if t['id'] == id), None)
    if turma:
        return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404

@app.route('/turmas/<int:id>', methods=['PUT'])
def update_turma(id):
    data = request.get_json()
    turma = next((t for t in turmas if t['id'] == id), None)
    if turma:
        if 'professor_id' in data and not any(p['id'] == data['professor_id'] for p in professores):
            return jsonify({"erro": "professor nao encontrado"}), 400
        turma.update(data)
        return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404

@app.route('/turmas/<int:id>', methods=['DELETE'])
def delete_turma(id):
    global turmas
    turmas = [t for t in turmas if t['id'] != id]
    return jsonify({"message": "Turma deletada com sucesso"})

@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(alunos)

@app.route('/alunos', methods=['POST'])
def add_aluno():
    data = request.get_json()
    if 'nome' not in data:
        return jsonify({"erro": "aluno sem nome"}), 400
    if 'idade' not in data or data['idade'] <= 0:
        return jsonify({"erro": "idade invalida"}), 400
    if 'data_nascimento' not in data or not validar_data(data['data_nascimento']):
        return jsonify({"erro": "data de nascimento invalida ou ausente"}), 400
    if 'turma_id' not in data or not any(t['id'] == data['turma_id'] for t in turmas):
        return jsonify({"erro": "turma nao encontrada"}), 400
    if 'nota_primeiro_semestre' in data and 'nota_segundo_semestre' in data:
        data['media_final'] = (data['nota_primeiro_semestre'] + data['nota_segundo_semestre']) / 2
    if any(a['id'] == data['id'] for a in alunos):
        return jsonify({"erro": "id ja utilizada"}), 400
    alunos.append(data)
    return jsonify(data), 201

@app.route('/alunos/<int:id>', methods=['GET'])
def get_aluno(id):
    aluno = next((a for a in alunos if a['id'] == id), None)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "aluno nao encontrado"}), 404

@app.route('/alunos/<int:id>', methods=['PUT'])
def update_aluno(id):
    data = request.get_json()
    aluno = next((a for a in alunos if a['id'] == id), None)
    if aluno is None:
        return jsonify({"erro": "aluno nao encontrado"}), 404
    if 'nome' not in data:
        return jsonify({"erro": "aluno sem nome"}), 400
    if 'data_nascimento' in data and not validar_data(data['data_nascimento']):
        return jsonify({"erro": "data de nascimento invalida"}), 400
    if 'turma_id' in data and not any(t['id'] == data['turma_id'] for t in turmas):
        return jsonify({"erro": "turma nao encontrada"}), 400
    
    aluno.update(data)
    
    if 'nota_primeiro_semestre' in data or 'nota_segundo_semestre' in data:
        nota1 = data.get('nota_primeiro_semestre', aluno.get('nota_primeiro_semestre', 0))
        nota2 = data.get('nota_segundo_semestre', aluno.get('nota_segundo_semestre', 0))
        aluno['media_final'] = (nota1 + nota2) / 2
    
    return jsonify(aluno)

@app.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    global alunos
    if not any(a['id'] == id for a in alunos):
        return jsonify({"erro": "aluno nao encontrado"}), 404
    alunos = [a for a in alunos if a['id'] != id]
    return jsonify({"message": "Aluno deletado com sucesso"})

@app.route('/turmas/<int:turma_id>/alunos', methods=['GET'])
def get_alunos_por_turma(turma_id):
    if not any(t['id'] == turma_id for t in turmas):
        return jsonify({"erro": "turma nao encontrada"}), 404
    alunos_turma = [a for a in alunos if a.get('turma_id') == turma_id]
    return jsonify(alunos_turma)

@app.route('/professores/<int:professor_id>/turmas', methods=['GET'])
def get_turmas_por_professor(professor_id):
    if not any(p['id'] == professor_id for p in professores):
        return jsonify({"erro": "professor nao encontrado"}), 404
    turmas_professor = [t for t in turmas if t.get('professor_id') == professor_id]
    return jsonify(turmas_professor)

@app.route('/professores/<int:professor_id>/alunos', methods=['GET'])
def get_alunos_por_professor(professor_id):
    if not any(p['id'] == professor_id for p in professores):
        return jsonify({"erro": "professor nao encontrado"}), 404
    
    turmas_professor = [t['id'] for t in turmas if t.get('professor_id') == professor_id]
    
    alunos_professor = [a for a in alunos if a.get('turma_id') in turmas_professor]
    
    return jsonify(alunos_professor)

@app.route('/reseta', methods=['POST'])
def reseta_dados():
    global professores, turmas, alunos
    professores = []
    turmas = []
    alunos = []
    return jsonify({"message": "Todos os dados foram resetados com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from controllers.alunos_controller import aluno_bp
from controllers.professores_controller import professor_bp
from controllers.turmas_controller import turma_bp

from controllers.reset_controller import reset_bp

from config import db
from flasgger import Swagger

app = Flask(__name__)



app.config['PORT'] = 5000
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SWAGGER'] = {
    "title": "DevAPI - Documentação com Swagger",
    "uiversion": 3
}


db.init_app(app)
swagger = Swagger(app)


app.register_blueprint(aluno_bp, url_prefix="/alunos")
app.register_blueprint(professor_bp, url_prefix="/professores")
app.register_blueprint(turma_bp, url_prefix="/turmas")

db.init_app(app)
swagger = Swagger(app)


app.register_blueprint(aluno_bp, url_prefix="/alunos")
app.register_blueprint(professor_bp, url_prefix="/professores")
app.register_blueprint(turma_bp, url_prefix="/turmas")

app.register_blueprint(reset_bp)  



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

def teste():
    return {"message": "Tudo está funcionando corretamente!"}


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

    return '🚀 Bem-vindo à API DevAPI! Acesse a documentação Swagger em /apidocs/'


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

    app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, jsonify, request

# Inicializa a aplicação Flask
app = Flask(__name__)

# Listas para armazenar os dados temporariamente (simulando um banco de dados)
professores = []
turmas = []
alunos = []

# Endpoints CRUD para Professores
@app.route('/professores', methods=['GET'])
def get_professores():
    return jsonify(professores)

@app.route('/professores', methods=['POST'])
def add_professor():
    data = request.get_json()
    if 'nome' not in data:
        return jsonify({"erro": "professor sem nome"}), 400
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

# Endpoints CRUD para Turmas
@app.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify(turmas)

@app.route('/turmas', methods=['POST'])
def add_turma():
    data = request.get_json()
    if 'descricao' not in data:
        return jsonify({"erro": "turma sem descricao"}), 400
    if any(t['id'] == data['id'] for t in turmas):
        return jsonify({"erro": "id ja utilizada"}), 400
    turmas.append(data)
    return jsonify(data), 201

@app.route('/turmas/<int:id>', methods=['GET'])
def get_turma(id):
    turma = next((t for t in turmas if t['id'] == id), None)
    if turma:
        return jsonify(turma)
    return jsonify({"message": "Turma não encontrada"}), 404

@app.route('/turmas/<int:id>', methods=['PUT'])
def update_turma(id):
    data = request.get_json()
    turma = next((t for t in turmas if t['id'] == id), None)
    if turma:
        turma.update(data)
        return jsonify(turma)
    return jsonify({"message": "Turma não encontrada"}), 404

@app.route('/turmas/<int:id>', methods=['DELETE'])
def delete_turma(id):
    global turmas
    turmas = [t for t in turmas if t['id'] != id]
    return jsonify({"message": "Turma deletada com sucesso"})

# Endpoints CRUD para Alunos
@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(alunos)

@app.route('/alunos', methods=['POST'])
def add_aluno():
    data = request.get_json()
    if 'nome' not in data:
        return jsonify({"erro": "aluno sem nome"}), 400
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
    aluno.update(data)
    return jsonify(aluno)

@app.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    global alunos
    if not any(a['id'] == id for a in alunos):
        return jsonify({"erro": "aluno nao encontrado"}), 404
    alunos = [a for a in alunos if a['id'] != id]
    return jsonify({"message": "Aluno deletado com sucesso"})

@app.route('/reseta', methods=['POST'])
def reseta_dados():
    global professores, turmas, alunos
    professores = []
    turmas = []
    alunos = []
    return jsonify({"message": "Todos os dados foram resetados com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, request

app = Flask(__name__)

# Listas para armazenar os dados (substituindo um banco de dados)
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
    professores.append(data)
    return jsonify(data), 201

@app.route('/professores/<int:id>', methods=['GET'])
def get_professor(id):
    professor = next((p for p in professores if p['id'] == id), None)
    if professor:
        return jsonify(professor)
    return jsonify({"message": "Professor não encontrado"}), 404

@app.route('/professores/<int:id>', methods=['PUT'])
def update_professor(id):
    data = request.get_json()
    professor = next((p for p in professores if p['id'] == id), None)
    if professor:
        professor.update(data)
        return jsonify(professor)
    return jsonify({"message": "Professor não encontrado"}), 404

@app.route('/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    global professores
    professores = [p for p in professores if p['id'] != id]
    return jsonify({"message": "Professor deletado com sucesso"})

# Endpoints CRUD para Turmas
@app.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify(turmas)

@app.route('/turmas', methods=['POST'])
def add_turma():
    data = request.get_json()
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
    alunos.append(data)
    return jsonify(data), 201

@app.route('/alunos/<int:id>', methods=['GET'])
def get_aluno(id):
    aluno = next((a for a in alunos if a['id'] == id), None)
    if aluno:
        return jsonify(aluno)
    return jsonify({"message": "Aluno não encontrado"}), 404

@app.route('/alunos/<int:id>', methods=['PUT'])
def update_aluno(id):
    data = request.get_json()
    aluno = next((a for a in alunos if a['id'] == id), None)
    if aluno:
        aluno.update(data)
        return jsonify(aluno)
    return jsonify({"message": "Aluno não encontrado"}), 404

@app.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    global alunos
    alunos = [a for a in alunos if a['id'] != id]
    return jsonify({"message": "Aluno deletado com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)
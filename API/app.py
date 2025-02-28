from flask import Flask, jsonify, request

# Inicializa a aplicação Flask
app = Flask(__name__)

# Listas para armazenar os dados temporariamente (simulando um banco de dados)
professores = []  # Lista para armazenar os professores
turmas = []  # Lista para armazenar as turmas
alunos = []  # Lista para armazenar os alunos

# Endpoints CRUD para Professores
@app.route('/professores', methods=['GET'])
def get_professores():
    """Retorna a lista de todos os professores."""
    return jsonify(professores)

@app.route('/professores', methods=['POST'])
def add_professor():
    """Adiciona um novo professor à lista."""
    data = request.get_json()  # Obtém os dados do corpo da requisição
    professores.append(data)  # Adiciona o professor à lista
    return jsonify(data), 201  # Retorna os dados adicionados e o status 201 (Criado)

@app.route('/professores/<int:id>', methods=['GET'])
def get_professor(id):
    """Retorna um professor específico pelo ID."""
    professor = next((p for p in professores if p['id'] == id), None)  # Busca o professor pelo ID
    if professor:
        return jsonify(professor)  # Retorna os dados do professor
    return jsonify({"message": "Professor não encontrado"}), 404  # Retorna erro 404 se não encontrado

@app.route('/professores/<int:id>', methods=['PUT'])
def update_professor(id):
    """Atualiza os dados de um professor pelo ID."""
    data = request.get_json()
    professor = next((p for p in professores if p['id'] == id), None)
    if professor:
        professor.update(data)  # Atualiza os dados do professor
        return jsonify(professor)
    return jsonify({"message": "Professor não encontrado"}), 404

@app.route('/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    """Remove um professor da lista pelo ID."""
    global professores
    professores = [p for p in professores if p['id'] != id]  # Remove o professor da lista
    return jsonify({"message": "Professor deletado com sucesso"})

# Endpoints CRUD para Turmas
@app.route('/turmas', methods=['GET'])
def get_turmas():
    """Retorna a lista de todas as turmas."""
    return jsonify(turmas)

@app.route('/turmas', methods=['POST'])
def add_turma():
    """Adiciona uma nova turma à lista."""
    data = request.get_json()
    turmas.append(data)
    return jsonify(data), 201

@app.route('/turmas/<int:id>', methods=['GET'])
def get_turma(id):
    """Retorna uma turma específica pelo ID."""
    turma = next((t for t in turmas if t['id'] == id), None)
    if turma:
        return jsonify(turma)
    return jsonify({"message": "Turma não encontrada"}), 404

@app.route('/turmas/<int:id>', methods=['PUT'])
def update_turma(id):
    """Atualiza os dados de uma turma pelo ID."""
    data = request.get_json()
    turma = next((t for t in turmas if t['id'] == id), None)
    if turma:
        turma.update(data)
        return jsonify(turma)
    return jsonify({"message": "Turma não encontrada"}), 404

@app.route('/turmas/<int:id>', methods=['DELETE'])
def delete_turma(id):
    """Remove uma turma da lista pelo ID."""
    global turmas
    turmas = [t for t in turmas if t['id'] != id]
    return jsonify({"message": "Turma deletada com sucesso"})

# Endpoints CRUD para Alunos
@app.route('/alunos', methods=['GET'])
def get_alunos():
    """Retorna a lista de todos os alunos."""
    return jsonify(alunos)

@app.route('/alunos', methods=['POST'])
def add_aluno():
    """Adiciona um novo aluno à lista."""
    data = request.get_json()
    alunos.append(data)
    return jsonify(data), 201

@app.route('/alunos/<int:id>', methods=['GET'])
def get_aluno(id):
    """Retorna um aluno específico pelo ID."""
    aluno = next((a for a in alunos if a['id'] == id), None)
    if aluno:
        return jsonify(aluno)
    return jsonify({"message": "Aluno não encontrado"}), 404

@app.route('/alunos/<int:id>', methods=['PUT'])
def update_aluno(id):
    """Atualiza os dados de um aluno pelo ID."""
    data = request.get_json()
    aluno = next((a for a in alunos if a['id'] == id), None)
    if aluno:
        aluno.update(data)
        return jsonify(aluno)
    return jsonify({"message": "Aluno não encontrado"}), 404

@app.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    """Remove um aluno da lista pelo ID."""
    global alunos
    alunos = [a for a in alunos if a['id'] != id]
    return jsonify({"message": "Aluno deletado com sucesso"})

if __name__ == '__main__':
    # Executa a aplicação em modo de debug para facilitar o desenvolvimento
    app.run(debug=True)

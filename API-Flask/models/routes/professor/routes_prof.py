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
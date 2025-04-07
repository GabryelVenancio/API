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

@app.route('/turmas/<int:turma_id>/alunos', methods=['GET'])
def get_alunos_por_turma(turma_id):
    if not any(t['id'] == turma_id for t in turmas):
        return jsonify({"erro": "turma nao encontrada"}), 404
    alunos_turma = [a for a in alunos if a.get('turma_id') == turma_id]
    return jsonify(alunos_turma)
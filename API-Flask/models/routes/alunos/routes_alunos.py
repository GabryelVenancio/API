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
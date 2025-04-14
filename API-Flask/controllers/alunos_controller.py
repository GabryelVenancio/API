from flask import Blueprint, jsonify, request
from models.alunos.alunos import criar_aluno, listar_alunos, buscar_aluno_por_id

alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(listar_alunos())

@alunos_bp.route('/alunos', methods=['POST'])
def add_aluno():
    data = request.get_json()
    if 'nome' not in data:
        return jsonify({"erro": "aluno sem nome"}), 400
    aluno = criar_aluno(data['nome'])
    return jsonify(aluno), 201

@alunos_bp.route('/alunos/<int:id>', methods=['GET'])
def get_aluno(id):
    aluno = buscar_aluno_por_id(id)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

@alunos_bp.route('/alunos/<int:id>', methods=['PUT'])
def update_aluno(id):
    data = request.get_json()
    aluno = buscar_aluno_por_id(id)
    if aluno:
        aluno.update(data)
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

@alunos_bp.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    global alunos
    alunos = [a for a in alunos if a['id'] != id]
    return jsonify({"message": "Aluno deletado com sucesso"})

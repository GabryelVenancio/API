from flask import Blueprint, jsonify, request
from models.turmas.turmas import criar_turma, listar_turmas, buscar_turma_por_id
from models.professores.professores import buscar_professor_por_id
from models.alunos.alunos import listar_alunos

turmas_bp = Blueprint('turmas', __name__)

@turmas_bp.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify(listar_turmas())

@turmas_bp.route('/turmas', methods=['POST'])
def add_turma():
    data = request.get_json()
    if 'nome' not in data:
        return jsonify({"erro": "turma sem nome"}), 400
    if 'professor_id' not in data or not buscar_professor_por_id(data['professor_id']):
        return jsonify({"erro": "professor nao encontrado"}), 400
    turma = criar_turma(data['nome'])
    return jsonify(turma), 201

@turmas_bp.route('/turmas/<int:id>', methods=['GET'])
def get_turma(id):
    turma = buscar_turma_por_id(id)
    if turma:
        return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404

@turmas_bp.route('/turmas/<int:id>', methods=['PUT'])
def update_turma(id):
    data = request.get_json()
    turma = buscar_turma_por_id(id)
    if turma:
        turma.update(data)
        return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404

@turmas_bp.route('/turmas/<int:id>', methods=['DELETE'])
def delete_turma(id):
    global turmas
    turmas = [t for t in turmas if t['id'] != id]
    return jsonify({"message": "Turma deletada com sucesso"})

@turmas_bp.route('/turmas/<int:turma_id>/alunos', methods=['GET'])
def get_alunos_por_turma(turma_id):
    turma = buscar_turma_por_id(turma_id)
    if turma:
        alunos_turma = [a for a in listar_alunos() if a.get('turma_id') == turma_id]
        return jsonify(alunos_turma)
    return jsonify({"erro": "Turma não encontrada"}), 404
from flask import Blueprint, jsonify, request
from models.professores.professores import criar_professor, listar_professores, buscar_professor_por_id

professores_bp = Blueprint('professores', __name__)

@professores_bp.route('/professores', methods=['GET'])
def get_professores():
    return jsonify(listar_professores())

@professores_bp.route('/professores', methods=['POST'])
def add_professor():
    data = request.get_json()
    if 'nome' not in data:
        return jsonify({"erro": "professor sem nome"}), 400
    professor = criar_professor(data['nome'])
    return jsonify(professor), 201

@professores_bp.route('/professores/<int:id>', methods=['GET'])
def get_professor(id):
    professor = buscar_professor_por_id(id)
    if professor:
        return jsonify(professor)
    return jsonify({"erro": "Professor não encontrado"}), 404

@professores_bp.route('/professores/<int:id>', methods=['PUT'])
def update_professor(id):
    data = request.get_json()
    professor = buscar_professor_por_id(id)
    if professor:
        professor.update(data)
        return jsonify(professor)
    return jsonify({"erro": "Professor não encontrado"}), 404

@professores_bp.route('/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    global professores
    professores = [p for p in professores if p['id'] != id]
    return jsonify({"message": "Professor deletado com sucesso"})
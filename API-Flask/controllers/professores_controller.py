from flask import Blueprint, request, jsonify
from models.professores import (
    criar_professor, listar_professores, buscar_professor_por_id,
    atualizar_professor, deletar_professor
)
from flasgger import swag_from

professor_bp = Blueprint("professores", __name__)

@professor_bp.route("/", methods=["GET"])
@swag_from({'tags': ['PROFESSORES']})
def get_professores():
    professores = listar_professores()
    return jsonify([{"id": p.id, "nome": p.nome, "especialidade": p.especialidade} for p in professores])

@professor_bp.route("/", methods=["POST"])
@swag_from({'tags': ['PROFESSORES']})
def post_professor():
    data = request.form
    professor = criar_professor(data['nome'], data['especialidade'])
    return jsonify({"id": professor.id, "nome": professor.nome, "especialidade": professor.especialidade}), 201

@professor_bp.route("/<int:professor_id>", methods=["GET"])
@swag_from({'tags': ['PROFESSORES']})
def get_professor_por_id(professor_id):
    professor = buscar_professor_por_id(professor_id)
    if professor:
        return jsonify({"id": professor.id, "nome": professor.nome, "especialidade": professor.especialidade})
    return jsonify({"erro": "Professor não encontrado"}), 404

@professor_bp.route("/<int:professor_id>", methods=["PUT"])
@swag_from({'tags': ['PROFESSORES']})
def put_professor(professor_id):
    data = request.form
    professor = atualizar_professor(professor_id, data['nome'], data['especialidade'])
    if professor:
        return jsonify({"id": professor.id, "nome": professor.nome, "especialidade": professor.especialidade})
    return jsonify({"erro": "Professor não encontrado"}), 404

@professor_bp.route("/<int:professor_id>", methods=["DELETE"])
@swag_from({'tags': ['PROFESSORES']})
def delete_professor(professor_id):
    professor = deletar_professor(professor_id)
    if professor:
        return jsonify({"mensagem": "Professor deletado com sucesso"})
    return jsonify({"erro": "Professor não encontrado"}), 404
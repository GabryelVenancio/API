from flask import Blueprint, request, jsonify
from models.turmas import (
    criar_turma, listar_turmas, buscar_turma_por_id,
    atualizar_turma, deletar_turma
)
from flasgger import swag_from

turma_bp = Blueprint("turmas", __name__)

@turma_bp.route("/", methods=["GET"])
@swag_from({'tags': ['TURMAS']})
def get_turmas():
    turmas = listar_turmas()
    return jsonify([{"id": t.id, "nome": t.nome, "turno": t.turno} for t in turmas])

@turma_bp.route("/", methods=["POST"])
@swag_from({'tags': ['TURMAS']})
def post_turma():
    data = request.form
    turma = criar_turma(data['nome'], data['turno'])
    return jsonify({"id": turma.id, "nome": turma.nome, "turno": turma.turno}), 201

@turma_bp.route("/<int:turma_id>", methods=["GET"])
@swag_from({'tags': ['TURMAS']})
def get_turma_por_id(turma_id):
    turma = buscar_turma_por_id(turma_id)
    if turma:
        return jsonify({"id": turma.id, "nome": turma.nome, "turno": turma.turno})
    return jsonify({"erro": "Turma não encontrada"}), 404

@turma_bp.route("/<int:turma_id>", methods=["PUT"])
@swag_from({'tags': ['TURMAS']})
def put_turma(turma_id):
    data = request.form
    turma = atualizar_turma(turma_id, data['nome'], data['turno'])
    if turma:
        return jsonify({"id": turma.id, "nome": turma.nome, "turno": turma.turno})
    return jsonify({"erro": "Turma não encontrada"}), 404

@turma_bp.route("/<int:turma_id>", methods=["DELETE"])
@swag_from({'tags': ['TURMAS']})
def delete_turma(turma_id):
    turma = deletar_turma(turma_id)
    if turma:
        return jsonify({"mensagem": "Turma deletada com sucesso"})
    return jsonify({"erro": "Turma não encontrada"}), 404
from flask import Blueprint, request, jsonify
from models.alunos import (
    criar_aluno, listar_alunos, buscar_aluno_por_id,
    atualizar_aluno, deletar_aluno
)
from flasgger import swag_from

aluno_bp = Blueprint("alunos", __name__)

@aluno_bp.route("/", methods=["GET"])
@swag_from({
    'tags': ['ALUNOS'],
    'responses': {
        200: {
            'description': 'Lista de alunos retornada com sucesso'
        }
    }
})
def get_alunos():
    alunos = listar_alunos()
    return jsonify([{"id": a.id, "nome": a.nome, "email": a.email} for a in alunos])

@aluno_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['ALUNOS'],
    'parameters': [
        {'name': 'nome', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'email', 'in': 'formData', 'type': 'string', 'required': True},
    ],
    'responses': {201: {'description': 'Aluno criado com sucesso'}}
})
def post_aluno():
    data = request.form
    aluno = criar_aluno(data['nome'], data['email'])
    return jsonify({"id": aluno.id, "nome": aluno.nome, "email": aluno.email}), 201

@aluno_bp.route("/<int:aluno_id>", methods=["GET"])
@swag_from({'tags': ['ALUNOS']})
def get_aluno_por_id(aluno_id):
    aluno = buscar_aluno_por_id(aluno_id)
    if aluno:
        return jsonify({"id": aluno.id, "nome": aluno.nome, "email": aluno.email})
    return jsonify({"erro": "Aluno não encontrado"}), 404

@aluno_bp.route("/<int:aluno_id>", methods=["PUT"])
@swag_from({'tags': ['ALUNOS']})
def put_aluno(aluno_id):
    data = request.form
    aluno = atualizar_aluno(aluno_id, data['nome'], data['email'])
    if aluno:
        return jsonify({"id": aluno.id, "nome": aluno.nome, "email": aluno.email})
    return jsonify({"erro": "Aluno não encontrado"}), 404

@aluno_bp.route("/<int:aluno_id>", methods=["DELETE"])
@swag_from({'tags': ['ALUNOS']})
def delete_aluno(aluno_id):
    aluno = deletar_aluno(aluno_id)
    if aluno:
        return jsonify({"mensagem": "Aluno deletado com sucesso"})
    return jsonify({"erro": "Aluno não encontrado"}), 404
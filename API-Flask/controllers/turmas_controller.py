from flask import Blueprint, request, jsonify
<<<<<<< HEAD
from models.turmas import criar_turma, listar_turmas, buscar_turma_por_id, deletar_turma, atualizar_turma
from flasgger import swag_from

turma_bp = Blueprint("turma_bp", __name__)

# GET /turmas
@turma_bp.route("/", methods=["GET"])
@swag_from({
    'tags': ['TURMAS'],
    'responses': {
        200: {
            'description': 'Lista de turmas',
            'examples': {
                'application/json': [
                    {'id': 1, 'nome': 'Turma A', 'codigo': 'TURMA-A', 'ano': 2023},
                    {'id': 2, 'nome': 'Turma B', 'codigo': 'TURMA-B', 'ano': 2023}
                ]
            }
        }
    }
})
def get_turmas():
    turmas = listar_turmas()
    return jsonify(turmas)

# POST /turmas
@turma_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['TURMAS'],
    'parameters': [
        {
            'name': 'nome',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Nome da turma',
            'example': 'Turma A'
        },
        {
            'name': 'codigo',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Código da turma',
            'example': 'TURMA-A'
        },
        {
            'name': 'ano',
            'in': 'formData',
            'type': 'integer',
            'required': True,
            'description': 'Ano da turma',
            'example': 2023
        }
    ],
    'responses': {
        201: {
            'description': 'Turma criada com sucesso',
            'examples': {
                'application/json': {
                    'id': 1,
                    'nome': 'Turma A',
                    'codigo': 'TURMA-A',
                    'ano': 2023
                }
            }
        }
    }
})
def post_turma():
    nome = request.form.get("nome")
    codigo = request.form.get("codigo")
    ano = request.form.get("ano")
    turma = criar_turma(nome, codigo, ano)
    return jsonify(turma), 201

# GET /turmas/<id>
@turma_bp.route("/<int:id>", methods=["GET"])
@swag_from({
    'tags': ['TURMAS'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da turma',
            'example': 1
        }
    ],
    'responses': {
        200: {
            'description': 'Turma encontrada',
            'examples': {
                'application/json': {
                    'id': 1,
                    'nome': 'Turma A',
                    'codigo': 'TURMA-A',
                    'ano': 2023
                }
            }
        },
        404: {
            'description': 'Turma não encontrada'
        }
    }
})
def get_turma_por_id(id):
    turma = buscar_turma_por_id(id)
    if turma:
        return jsonify(turma)
    return jsonify({"message": "Turma não encontrada"}), 404

# PUT /turmas/<id>
@turma_bp.route("/<int:id>", methods=["PUT"])
@swag_from({
    'tags': ['TURMAS'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da turma',
            'example': 1
        },
        {
            'name': 'nome',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Nome da turma',
            'example': 'Turma A'
        },
        {
            'name': 'codigo',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Código da turma',
            'example': 'TURMA-A'
        },
        {
            'name': 'ano',
            'in': 'formData',
            'type': 'integer',
            'required': True,
            'description': 'Ano da turma',
            'example': 2023
        }
    ],
    'responses': {
        200: {
            'description': 'Turma atualizada com sucesso',
            'examples': {
                'application/json': {
                    'id': 1,
                    'nome': 'Turma A',
                    'codigo': 'TURMA-A',
                    'ano': 2023
                }
            }
        },
        404: {
            'description': 'Turma não encontrada'
        }
    }
})
def put_turma(id):
    nome = request.form.get("nome")
    codigo = request.form.get("codigo")
    ano = request.form.get("ano")
    turma = atualizar_turma(id, nome, codigo, ano)
    if turma:
        return jsonify(turma)
    return jsonify({"message": "Turma não encontrada"}), 404

# DELETE /turmas/<id>
@turma_bp.route("/<int:id>", methods=["DELETE"])
@swag_from({
    'tags': ['TURMAS'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da turma',
            'example': 1
        }
    ],
    'responses': {
        200: {
            'description': 'Turma deletada com sucesso'
        },
        404: {
            'description': 'Turma não encontrada'
        }
    }
})
def delete_turma(id):
    turma = deletar_turma(id)
    if turma:
        return jsonify({"message": "Turma deletada com sucesso"})
    return jsonify({"message": "Turma não encontrada"}), 404
=======
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
>>>>>>> 404414ebaed6bc112fa199b8b2c271353e5ed4a0

from flask import Blueprint, request, jsonify
<<<<<<< HEAD
from models.professores import criar_professor, listar_professores, buscar_professor_por_id, deletar_professor, atualizar_professor
from flasgger import swag_from

professor_bp = Blueprint("professor_bp", __name__)

# GET /professores
@professor_bp.route("/", methods=["GET"])
@swag_from({
    'tags': ['PROFESSORES'],
    'responses': {
        200: {
            'description': 'Lista de professores',
            'examples': {
                'application/json': [
                    {'id': 1, 'nome': 'Ana Souza', 'email': 'ana@email.com'},
                    {'id': 2, 'nome': 'Carlos Silva', 'email': 'carlos@email.com'}
                ]
            }
        }
    }
})
def get_professores():
    professores = listar_professores()
    return jsonify(professores)

# POST /professores
@professor_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['PROFESSORES'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string', 'example': 'Ana Souza'},
                    'email': {'type': 'string', 'example': 'ana@email.com'}
                },
                'required': ['nome', 'email']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Professor criado com sucesso',
            'examples': {
                'application/json': {
                    'id': 1,
                    'nome': 'Ana Souza',
                    'email': 'ana@email.com'
                }
            }
        }
    }
})
def post_professor():
    data = request.get_json()
    nome = data.get("nome")
    email = data.get("email")
    professor = criar_professor(nome, email)
    return jsonify(professor), 201

# GET /professores/<id>
@professor_bp.route("/<int:id>", methods=["GET"])
@swag_from({
    'tags': ['PROFESSORES'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do professor',
            'example': 1
        }
    ],
    'responses': {
        200: {
            'description': 'Professor encontrado',
            'examples': {
                'application/json': {
                    'id': 1,
                    'nome': 'Ana Souza',
                    'email': 'ana@email.com'
                }
            }
        },
        404: {
            'description': 'Professor não encontrado'
        }
    }
})
def get_professor_por_id(id):
    professor = buscar_professor_por_id(id)
    if professor:
        return jsonify(professor)
    return jsonify({"message": "Professor não encontrado"}), 404

# PUT /professores/<id>
@professor_bp.route("/<int:id>", methods=["PUT"])
@swag_from({
    'tags': ['PROFESSORES'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do professor',
            'example': 1
        },
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string', 'example': 'Ana Souza'},
                    'email': {'type': 'string', 'example': 'ana@email.com'}
                },
                'required': ['nome', 'email']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Professor atualizado com sucesso',
            'examples': {
                'application/json': {
                    'id': 1,
                    'nome': 'Ana Souza',
                    'email': 'ana@email.com'
                }
            }
        },
        404: {
            'description': 'Professor não encontrado'
        }
    }
})
def put_professor(id):
    data = request.get_json()
    nome = data.get("nome")
    email = data.get("email")
    professor = atualizar_professor(id, nome, email)
    if professor:
        return jsonify(professor)
    return jsonify({"message": "Professor não encontrado"}), 404

# DELETE /professores/<id>
@professor_bp.route("/<int:id>", methods=["DELETE"])
@swag_from({
    'tags': ['PROFESSORES'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do professor',
            'example': 1
        }
    ],
    'responses': {
        200: {
            'description': 'Professor deletado com sucesso'
        },
        404: {
            'description': 'Professor não encontrado'
        }
    }
})
def delete_professor(id):
    professor = deletar_professor(id)
    if professor:
        return jsonify({"message": "Professor deletado com sucesso"})
    return jsonify({"message": "Professor não encontrado"}), 404
=======
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
>>>>>>> 404414ebaed6bc112fa199b8b2c271353e5ed4a0

from flask import Blueprint, request, jsonify
<<<<<<< HEAD
from models.alunos import criar_aluno, listar_alunos, buscar_aluno_por_id, deletar_aluno, atualizar_aluno
from flasgger import swag_from

aluno_bp = Blueprint("aluno_bp", __name__)
=======
from models.alunos import (
    criar_aluno, listar_alunos, buscar_aluno_por_id,
    atualizar_aluno, deletar_aluno
)
from flasgger import swag_from

aluno_bp = Blueprint("alunos", __name__)
>>>>>>> 404414ebaed6bc112fa199b8b2c271353e5ed4a0

@aluno_bp.route("/", methods=["GET"])
@swag_from({
    'tags': ['ALUNOS'],
    'responses': {
        200: {
<<<<<<< HEAD
            'description': 'Lista de alunos',
            'examples': {
                'application/json': [
                    {'id': 1, 'nome': 'Henry Modesto', 'email': 'henry@email.com'},
                    {'id': 2, 'nome': 'Gabryel Cleffs', 'email': 'gabryel@email.com'},
                    {'id': 3, 'nome': 'Andrey Thomaz', 'email': 'andrey@email.com'},
                    {'id': 4, 'nome': 'Mauricio', 'email': 'mauricio@email.com'}
                ]
            }
=======
            'description': 'Lista de alunos retornada com sucesso'
>>>>>>> 404414ebaed6bc112fa199b8b2c271353e5ed4a0
        }
    }
})
def get_alunos():
    alunos = listar_alunos()
<<<<<<< HEAD
    return jsonify(alunos)
=======
    return jsonify([{"id": a.id, "nome": a.nome, "email": a.email} for a in alunos])
>>>>>>> 404414ebaed6bc112fa199b8b2c271353e5ed4a0

@aluno_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['ALUNOS'],
    'parameters': [
<<<<<<< HEAD
        {
            'name': 'nome',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Nome do aluno',
            'example': 'Henry Modesto'
        },
        {
            'name': 'email',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'E-mail do aluno',
            'example': 'henry@email.com'
        }
    ],
    'responses': {
        201: {
            'description': 'Aluno criado com sucesso',
            'examples': {
                'application/json': {
                    'id': 1,
                    'nome': 'Henry Modesto',
                    'email': 'henry@email.com'
                }
            }
        }
    }
})
def post_aluno():
    nome = request.form.get("nome")
    email = request.form.get("email")
    aluno = criar_aluno(nome, email)
    return jsonify(aluno), 201

@aluno_bp.route("/<int:id>", methods=["GET"])
@swag_from({
    'tags': ['ALUNOS'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do aluno',
            'example': 1
        }
    ],
    'responses': {
        200: {
            'description': 'Aluno encontrado',
            'examples': {
                'application/json': {
                    'id': 1,
                    'nome': 'Henry Modesto',
                    'email': 'henry@email.com'
                }
            }
        },
        404: {
            'description': 'Aluno não encontrado'
        }
    }
})
def get_aluno_por_id(id):
    aluno = buscar_aluno_por_id(id)
    if aluno:
        return jsonify(aluno)
    return jsonify({"message": "Aluno não encontrado"}), 404


@aluno_bp.route("/<int:id>", methods=["PUT"])
@swag_from({
    'tags': ['ALUNOS'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do aluno',
            'example': 1
        },
        {
            'name': 'nome',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Nome do aluno',
            'example': 'Henry Modesto'
        },
        {
            'name': 'email',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'E-mail do aluno',
            'example': 'henry@email.com'
        }
    ],
    'responses': {
        200: {
            'description': 'Aluno atualizado com sucesso',
            'examples': {
                'application/json': {
                    'id': 1,
                    'nome': 'Henry Modesto',
                    'email': 'henry@email.com'
                }
            }
        },
        404: {
            'description': 'Aluno não encontrado'
        }
    }
})
def put_aluno(id):
    nome = request.form.get("nome")
    email = request.form.get("email")
    aluno = atualizar_aluno(id, nome, email)
    if aluno:
        return jsonify(aluno)
    return jsonify({"message": "Aluno não encontrado"}), 404


@aluno_bp.route("/<int:id>", methods=["DELETE"])
@swag_from({
    'tags': ['ALUNOS'],
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID do aluno',
            'example': 1
        }
    ],
    'responses': {
        200: {
            'description': 'Aluno deletado com sucesso'
        },
        404: {
            'description': 'Aluno não encontrado'
        }
    }
})
def delete_aluno(id):
    aluno = deletar_aluno(id)
    if aluno:
        return jsonify({"message": "Aluno deletado com sucesso"})
    return jsonify({"message": "Aluno não encontrado"}), 404
=======
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
>>>>>>> 404414ebaed6bc112fa199b8b2c271353e5ed4a0

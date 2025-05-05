from flask import Blueprint, request, jsonify
from models.professores.professores import (
    criar_professor,
    listar_professores,
    buscar_professor_por_id,
    atualizar_professor,
    deletar_professor
)
from flasgger import swag_from
from typing import Dict, List, Union

professor_bp = Blueprint("professores", __name__)

@professor_bp.route("/", methods=["GET"])
@swag_from({
    'tags': ['PROFESSORES'],
    'responses': {
        200: {
            'description': 'Lista de professores',
            'examples': {
                'application/json': [
                    {'id': 1, 'nome': 'Ana Souza', 'disciplina': 'Matemática'},
                    {'id': 2, 'nome': 'Carlos Silva', 'disciplina': 'História'}
                ]
            }
        }
    }
})
def get_professores() -> List[Dict[str, Union[int, str]]]:
    """Retorna todos os professores cadastrados."""
    professores = listar_professores()
    return jsonify([professor.to_dict() for professor in professores])

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
                    'disciplina': {'type': 'string', 'example': 'Matemática'}
                },
                'required': ['nome', 'disciplina']
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
                    'disciplina': 'Matemática'
                }
            }
        },
        400: {
            'description': 'Dados inválidos ou incompletos'
        }
    }
})
def post_professor() -> Dict[str, Union[int, str]]:
    """Cria um novo professor."""
    data = request.get_json()
    if not data:
        return jsonify({"message": "Dados não fornecidos"}), 400
        
    nome = data.get("nome")
    disciplina = data.get("disciplina")
    
    if not nome or not disciplina:
        return jsonify({"message": "Nome e disciplina são obrigatórios"}), 400
        
    professor = criar_professor(nome, disciplina)
    return jsonify(professor.to_dict()), 201

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
                    'disciplina': 'Matemática'
                }
            }
        },
        404: {
            'description': 'Professor não encontrado'
        }
    }
})
def get_professor_por_id(id: int) -> Dict[str, Union[int, str]]:
    """Retorna um professor específico pelo ID."""
    professor = buscar_professor_por_id(id)
    if professor:
        return jsonify(professor.to_dict())
    return jsonify({"message": "Professor não encontrado"}), 404

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
                    'disciplina': {'type': 'string', 'example': 'Matemática'}
                },
                'required': ['nome', 'disciplina']
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
                    'disciplina': 'Matemática'
                }
            }
        },
        400: {
            'description': 'Dados inválidos ou incompletos'
        },
        404: {
            'description': 'Professor não encontrado'
        }
    }
})
def put_professor(id: int) -> Dict[str, Union[int, str]]:
    """Atualiza os dados de um professor."""
    data = request.get_json()
    if not data:
        return jsonify({"message": "Dados não fornecidos"}), 400
        
    nome = data.get("nome")
    disciplina = data.get("disciplina")
    
    if not nome or not disciplina:
        return jsonify({"message": "Nome e disciplina são obrigatórios"}), 400
        
    professor = atualizar_professor(id, nome, disciplina)
    if professor:
        return jsonify(professor.to_dict())
    return jsonify({"message": "Professor não encontrado"}), 404

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
def delete_professor(id: int) -> Dict[str, str]:
    """Remove um professor do sistema."""
    professor = deletar_professor(id)
    if professor:
        return jsonify({"message": "Professor deletado com sucesso"})
    return jsonify({"message": "Professor não encontrado"}), 404
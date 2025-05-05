from flask import Blueprint, request, jsonify
from models.turmas.turmas import (
    criar_turma,
    listar_turmas,
    buscar_turma_por_id,
    atualizar_turma,
    deletar_turma
)
from flasgger import swag_from
from typing import Dict, List, Union

turma_bp = Blueprint("turmas", __name__)

@turma_bp.route("/", methods=["GET"])
@swag_from({
    'tags': ['TURMAS'],
    'responses': {
        200: {
            'description': 'Lista de turmas retornada com sucesso',
            'examples': {
                'application/json': [
                    {'id': 1, 'nome': 'Turma A', 'periodo': 'Manhã'},
                    {'id': 2, 'nome': 'Turma B', 'periodo': 'Tarde'}
                ]
            }
        }
    }
})
def get_turmas() -> List[Dict[str, Union[int, str]]]:
    """Retorna todas as turmas cadastradas."""
    turmas = listar_turmas()
    return jsonify([turma.to_dict() for turma in turmas])

@turma_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['TURMAS'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string', 'example': 'Turma A'},
                    'periodo': {'type': 'string', 'example': 'Manhã'}
                },
                'required': ['nome', 'periodo']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Turma criada com sucesso',
            'examples': {
                'application/json': {
                    'id': 1,
                    'nome': 'Turma A',
                    'periodo': 'Manhã'
                }
            }
        },
        400: {
            'description': 'Dados inválidos ou incompletos'
        }
    }
})
def post_turma() -> Dict[str, Union[int, str]]:
    """Cria uma nova turma."""
    data = request.get_json()
    if not data:
        return jsonify({"message": "Dados não fornecidos"}), 400
        
    nome = data.get("nome")
    periodo = data.get("periodo")
    
    if not nome or not periodo:
        return jsonify({"message": "Nome e período são obrigatórios"}), 400
        
    turma = criar_turma(nome, periodo)
    return jsonify(turma.to_dict()), 201

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
                    'periodo': 'Manhã'
                }
            }
        },
        404: {
            'description': 'Turma não encontrada'
        }
    }
})
def get_turma_por_id(id: int) -> Dict[str, Union[int, str]]:
    """Retorna uma turma específica pelo ID."""
    turma = buscar_turma_por_id(id)
    if turma:
        return jsonify(turma.to_dict())
    return jsonify({"message": "Turma não encontrada"}), 404

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
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'nome': {'type': 'string', 'example': 'Turma A'},
                    'periodo': {'type': 'string', 'example': 'Manhã'}
                },
                'required': ['nome', 'periodo']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Turma atualizada com sucesso',
            'examples': {
                'application/json': {
                    'id': 1,
                    'nome': 'Turma A',
                    'periodo': 'Manhã'
                }
            }
        },
        400: {
            'description': 'Dados inválidos ou incompletos'
        },
        404: {
            'description': 'Turma não encontrada'
        }
    }
})
def put_turma(id: int) -> Dict[str, Union[int, str]]:
    """Atualiza os dados de uma turma."""
    data = request.get_json()
    if not data:
        return jsonify({"message": "Dados não fornecidos"}), 400
        
    nome = data.get("nome")
    periodo = data.get("periodo")
    
    if not nome or not periodo:
        return jsonify({"message": "Nome e período são obrigatórios"}), 400
        
    turma = atualizar_turma(id, nome, periodo)
    if turma:
        return jsonify(turma.to_dict())
    return jsonify({"message": "Turma não encontrada"}), 404

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
def delete_turma(id: int) -> Dict[str, str]:
    """Remove uma turma do sistema."""
    turma = deletar_turma(id)
    if turma:
        return jsonify({"message": "Turma deletada com sucesso"})
    return jsonify({"message": "Turma não encontrada"}), 404
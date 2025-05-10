from flask import Blueprint, request, jsonify
from models.turmas import (
    criar_turma,
    listar_turmas,
    buscar_turma_por_id,
    atualizar_turma,
    deletar_turma
)

turma_bp = Blueprint('turma', __name__)

@turma_bp.route('', methods=['GET'])
def listar_turmas():
    """
    Lista todas as turmas
    ---
    tags:
      - Turmas
    responses:
      200:
        description: Lista de turmas retornada com sucesso
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/components/schemas/Turma'
    """
    turmas = listar_turmas()
    return jsonify(turmas)

@turma_bp.route('', methods=['POST'])
def criar_turma():
    """
    Cria uma nova turma
    ---
    tags:
      - Turmas
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/TurmaInput'
    responses:
      201:
        description: Turma criada com sucesso
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Turma'
      400:
        description: Erro na requisição
    """
    data = request.get_json()
    resposta, status = criar_turma(data)
    return jsonify(resposta), status

@turma_bp.route('/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    """
    Atualiza uma turma existente
    ---
    tags:
      - Turmas
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
        description: ID da turma a ser atualizada
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/TurmaInput'
    responses:
      200:
        description: Turma atualizada com sucesso
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Turma'
      400:
        description: Erro na validação dos dados
      404:
        description: Turma não encontrada
    """
    data = request.get_json()
    resposta, status = atualizar_turma(id, data)
    return jsonify(resposta), status

@turma_bp.route('/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    """
    Remove uma turma pelo ID
    ---
    tags:
      - Turmas
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
        description: ID da turma a ser removida
    responses:
      200:
        description: Turma removida com sucesso
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Turma removida com sucesso"
      404:
        description: Turma não encontrada
    """
    resposta, status = deletar_turma(id)
    return jsonify(resposta), status
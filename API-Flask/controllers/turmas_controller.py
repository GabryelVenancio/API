from flask import Blueprint, request, jsonify
from models.turmas import (
    criar_turma as model_criar_turmas,
    listar_turmas as model_listar_turmas,
    atualizar_turma as model_atualizar_turmas,
    deletar_turma as model_deletar_turmas
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
    turmas = model_listar_turmas()
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
    
    # Verificação de campos obrigatórios
    required_fields = ['descricao', 'professor_id']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Campo {field} é obrigatório'}), 400

    resposta, status = model_criar_turmas(data)
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
    resposta, status = model_atualizar_turmas(id, data)
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
    resposta, status = model_deletar_turmas(id)
    return jsonify(resposta), status

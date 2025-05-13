from flask import Blueprint, request, jsonify
from models.professores import (
    criar_professor as model_criar_professor,
    listar_professores as model_listar_professores,
    buscar_professor_por_id,
    atualizar_professor as model_atualizar_professor,
    deletar_professor as model_deletar_professor
)

professor_bp = Blueprint('professor', __name__)

@professor_bp.route('', methods=['GET'])
def listar_professores():
    """
    Lista todos os professores
    ---
    tags:
      - Professores
    responses:
      200:
        description: Lista de professores retornada com sucesso
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/components/schemas/Professor'
    """
    professores = model_listar_professores()
    return jsonify(professores)

@professor_bp.route('', methods=['POST'])
def criar_professor_route():
    """
    Cria um novo professor
    ---
    tags:
      - Professores
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProfessorInput'
    responses:
      201:
        description: Professor criado com sucesso
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Professor'
      400:
        description: Dados inválidos
      409:
        description: Professor já existe
    """
    data = request.get_json()
    if not data or not all(key in data for key in ['nome', 'idade', 'materia']):
        return jsonify({'error': 'Dados incompletos'}), 400
    
    resposta, status = model_criar_professor(data)
    return jsonify(resposta), status

@professor_bp.route('/<int:id>', methods=['GET'])
def obter_professor(id):
    """
    Obtém um professor pelo ID
    ---
    tags:
      - Professores
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Professor encontrado
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Professor'
      404:
        description: Professor não encontrado
    """
    professor = buscar_professor_por_id(id)
    if not professor:
        return jsonify({'error': 'Professor não encontrado'}), 404
    return jsonify(professor)

@professor_bp.route('/<int:id>', methods=['PUT'])
def atualizar_professor_route(id):
    """
    Atualiza um professor existente
    ---
    tags:
      - Professores
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ProfessorInput'
    responses:
      200:
        description: Professor atualizado com sucesso
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Professor'
      400:
        description: Dados inválidos
      404:
        description: Professor não encontrado
    """
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Nenhum dado fornecido'}), 400
    
    resposta, status = model_atualizar_professor(id, data)
    return jsonify(resposta), status

@professor_bp.route('/<int:id>', methods=['DELETE'])
def deletar_professor_route(id):
    """
    Remove um professor
    ---
    tags:
      - Professores
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Professor removido com sucesso
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Professor removido com sucesso"
      404:
        description: Professor não encontrado
      500:
        description: Erro interno ao remover professor
    """
    resposta, status = model_deletar_professor(id)
    return jsonify(resposta), status
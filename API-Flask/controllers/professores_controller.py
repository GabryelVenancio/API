from flask import Blueprint, request, jsonify
from models.professores import (
    criar_professor,
    listar_professores,
    buscar_professor_por_id,
    atualizar_professor,
    deletar_professor
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
    professores = listar_professores()
    return jsonify(professores)

@professor_bp.route('', methods=['POST'])
def criar_professor():
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
        description: Erro na requisição
    """
    data = request.get_json()
    resposta, status = criar_professor(data)
    return jsonify(resposta), status

@professor_bp.route('/<int:id>', methods=['PUT'])
def atualizar_professor(id):
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
        description: ID do professor a ser atualizado
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
        description: Erro na validação dos dados
      404:
        description: Professor não encontrado
    """
    data = request.get_json()
    resposta, status = atualizar_professor(id, data)
    return jsonify(resposta), status

@professor_bp.route('/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    """
    Remove um professor pelo ID
    ---
    tags:
      - Professores
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
        description: ID do professor a ser removido
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
    """
    resposta, status = deletar_professor(id)
    return jsonify(resposta), status
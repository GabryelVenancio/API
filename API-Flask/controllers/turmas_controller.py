from flask import Blueprint, jsonify, request
from models.turmas.turmas import criar_turma, listar_turmas, buscar_turma_por_id
from models.professores.professores import buscar_professor_por_id
from models.alunos.alunos import listar_alunos

turmas_bp = Blueprint('turmas', __name__)

turmas = listar_turmas()

@turmas_bp.route('/', methods=['GET'])
def get_turmas():
    """
    Lista todas as turmas
    ---
    responses:
      200:
        description: Lista de turmas retornada com sucesso
        content:
          application/json:
            example: [{"id": 1, "nome": "Turma A"}]
    """
    return jsonify(listar_turmas())

@turmas_bp.route('/', methods=['POST'])
def add_turma():
    """
    Cria uma nova turma
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            required:
              - nome
              - professor_id
            properties:
              nome:
                type: string
                example: "Turma B"
              professor_id:
                type: integer
                example: 1
    responses:
      201:
        description: Turma criada com sucesso
      400:
        description: Dados inválidos
    """
    data = request.get_json()
    if not data or 'nome' not in data:
        return jsonify({"erro": "turma sem nome"}), 400
    if 'professor_id' not in data or not buscar_professor_por_id(data['professor_id']):
        return jsonify({"erro": "professor nao encontrado"}), 400
    turma = criar_turma(data['nome'])
    return jsonify(turma), 201

@turmas_bp.route('/<int:id>', methods=['GET'])
def get_turma(id):
    """
    Retorna uma turma pelo ID
    ---
    parameters:
      - name: id
        in: path
        required: true
        description: ID da turma
        schema:
          type: integer
    responses:
      200:
        description: Turma encontrada
        content:
          application/json:
            example: {"id": 1, "nome": "Turma A"}
      404:
        description: Turma não encontrada
    """
    turma = buscar_turma_por_id(id)
    if turma:
        return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404

@turmas_bp.route('/<int:id>', methods=['PUT'])
def update_turma(id):
    """
    Atualiza os dados de uma turma
    ---
    parameters:
      - name: id
        in: path
        required: true
        description: ID da turma
        schema:
          type: integer
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              nome:
                type: string
                example: "Turma Atualizada"
    responses:
      200:
        description: Turma atualizada
      404:
        description: Turma não encontrada
    """
    data = request.get_json()
    turma = buscar_turma_por_id(id)
    if turma:
        turma.update(data)
        return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404

@turmas_bp.route('/<int:id>', methods=['DELETE'])
def delete_turma(id):
    """
    Deleta uma turma pelo ID
    ---
    parameters:
      - name: id
        in: path
        required: true
        description: ID da turma
        schema:
          type: integer
    responses:
      200:
        description: Turma deletada com sucesso
      404:
        description: Turma não encontrada
    """
    global turmas
    turma = buscar_turma_por_id(id)
    if turma:
        turmas = [t for t in turmas if t['id'] != id]
        return jsonify({"message": "Turma deletada com sucesso"})
    return jsonify({"erro": "Turma não encontrada"}), 404

@turmas_bp.route('/<int:turma_id>/alunos', methods=['GET'])
def get_alunos_por_turma(turma_id):
    """
    Lista os alunos de uma turma específica
    ---
    parameters:
      - name: turma_id
        in: path
        required: true
        description: ID da turma
        schema:
          type: integer
    responses:
      200:
        description: Lista de alunos da turma
        content:
          application/json:
            example: [{"id": 1, "nome": "João", "turma_id": 1}]
      404:
        description: Turma não encontrada
    """
    turma = buscar_turma_por_id(turma_id)
    if turma:
        alunos_turma = [a for a in listar_alunos() if a.get('turma_id') == turma_id]
        return jsonify(alunos_turma)
    return jsonify({"erro": "Turma não encontrada"}), 404
